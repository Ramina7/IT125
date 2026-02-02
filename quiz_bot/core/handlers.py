from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.quiz import Quiz

class BotHandlers:
    def __init__(self, bot):
        self.router = Router()
        self.bot = bot
        self.quiz = Quiz()
        self.user_data = {}
        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_quiz, Command("quiz"))
        self.router.callback_query.register(self.handle_answer)

    async def start_command(self, message: types.Message):
        await message.answer("Привет 👋\nЭто вторая версия викторины.\n/quiz — начать")

    async def start_quiz(self, message: types.Message):
        user_id = message.from_user.id
        self.user_data[user_id] = {"correct":0,"wrong":0,"q_index":0}
        await self.send_question(message.chat.id,user_id)

    async def send_question(self, chat_id, user_id):
        data = self.user_data[user_id]
        question_data = self.quiz.get_question(data["q_index"])
        if not question_data:
            await self.finish_quiz(chat_id,user_id)
            return

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=opt,callback_data=opt)] for opt in question_data["options"]]
        )
        await self.bot.send_photo(chat_id,question_data["image"],caption=question_data["question"],reply_markup=keyboard)

    async def handle_answer(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data = self.user_data.get(user_id)
        if not data:
            await callback.answer("Запусти /quiz")
            return

        question_data = self.quiz.get_question(data["q_index"])
        if callback.data == question_data["correct"]:
            data["correct"] += 1
        else:
            data["wrong"] += 1

        data["q_index"] += 1
        await callback.answer("Принято")
        await self.send_question(callback.message.chat.id,user_id)

    async def finish_quiz(self, chat_id, user_id):
        data = self.user_data[user_id]
        await self.bot.send_message(
            chat_id,
            f"🏁 Конец викторины\n✅ Правильных: {data['correct']}\n❌ Неправильных: {data['wrong']}"
        )
        del self.user_data[user_id]