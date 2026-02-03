import random
import asyncio

class RussianRoulette2Players:
    def __init__(self):
        self.chambers = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.chambers)
        self.current_index = 0
        self.is_alive = True
        self.score = {"Карина": 0, "Алина": 0}
        self.players = ["Карина", "Алина"]  
        self.current_player_index = 0
        self.time_limit = 5  

    @property
    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = 1 - self.current_player_index

    def shoot(self):
        if not self.is_alive:
            return "Игра окончена!"

        result = self.chambers[self.current_index]
        self.current_index += 1

        if result == 1:
            self.is_alive = False
            return "boom"
        else:
            self.score[self.current_player] += 1
            self.next_player()
            return "click"

    async def shoot_with_timeout(self):
        """Имитация таймера. Если игрок не успевает за 5 сек, проигрыш."""
        try:
            await asyncio.sleep(self.time_limit)
            if self.is_alive:
                self.is_alive = False
                return "timeout"
        except asyncio.CancelledError:
            return None
