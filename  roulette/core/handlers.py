from aiogram import Router, types
from aiogram.filters import Command
from core.roulette import RussianRoulette2Players
import asyncio

class BotHandlers:
    def __init__(self, bot):
        self.router = Router()
        self.bot = bot
        self.roulette_games = {}  
        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_roulette, Command("roulette"))
        self.router.message.register(self.shoot_roulette, Command("shoot"))
        self.router.message.register(self.stop_roulette, Command("stop"))

    async def start_command(self, message: types.Message):
        await message.answer(
            "Привет 👋\n"
            "Напиши команду /roulette чтобы начать игру в русскую рулетку 🎯"
        )

    async def start_roulette(self, message: types.Message):
        game = RussianRoulette2Players()
        self.roulette_games[message.chat.id] = game

        await message.answer(
            f"Игра началась!\n"
            f"Игроки: {game.players[0]} и {game.players[1]}\n"
            f"Ходит {game.current_player}. В барабане 1 патрон из 6.\n"
            f"Нажмите /shoot чтобы выстрелить! У вас есть 5 секунд на ход."
        )

    async def shoot_roulette(self, message: types.Message):
        game = self.roulette_games.get(message.chat.id)
        if not game or not game.is_alive:
            await message.answer("Сначала начни игру командой /roulette")
            return

        result = game.shoot()

        if result == "click":
            await message.answer(
                f"{game.current_player} выстрелил — Пусто!\n"
                f"Очки: {game.score}\n"
                f"Следующий ход: {game.current_player}"
            )

        elif result == "boom":
            await message.answer(
                f"{game.current_player} выстрелил — БУМ! Игра окончена!\n"
                f"Очки: {game.score}"
            )
            del self.roulette_games[message.chat.id]

    async def stop_roulette(self, message: types.Message):
        game = self.roulette_games.get(message.chat.id)
        if not game:
            await message.answer("Игра не запущена!")
            return
        await message.answer(f"Игра принудительно остановлена. Очки: {game.score}")
        del self.roulette_games[message.chat.id]
