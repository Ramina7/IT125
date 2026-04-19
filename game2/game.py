import random


class Game:
    def __init__(self):
        self.max_lives = 3
        self.reset()

    def reset(self):
        self.bullet_positions = random.sample(range(1, 7), 2)

        self.current_position = 1
        self.lives = self.max_lives
        self.alive = True

    def shot(self):
        if not self.alive:
            return "game over"

        if self.current_position in self.bullet_positions:
            self.lives -= 1

            if self.lives <= 0:
                self.alive = False
                return "boom"

            self.current_position += 1
            return "hit"

        self.current_position += 1
        return "empty"