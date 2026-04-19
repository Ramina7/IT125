import flet as ft
from game import Game
from ui import UI


class RouletteApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Русская рулетка"
        self.page.window_width = 400
        self.page.window_height = 500

        self.game = Game()
        self.ui = UI()

        self.ui.shoot_btn.on_click = self.shoot
        self.ui.reset_btn.on_click = self.reset

        self.page.add(*self.ui.build())

    def update_lives(self):
        self.ui.lives.value = "❤️ " * self.game.lives

    def shoot(self, e):
        if not self.game.alive:
            return

        try:
            self.ui.sound.play()
        except:
            pass

        result = self.game.shot()

        if result == "boom":
            self.ui.status.value = "💥 BOOM! Ты проиграл"
            self.ui.status.color = "red"

        elif result == "hit":
            self.ui.status.value = "💥 Попадание! -1 жизнь"
            self.ui.status.color = "orange"

        else:
            self.ui.status.value = "😅 Пусто"
            self.ui.status.color = "green"

        self.update_lives()
        self.ui.round.value = f"Раунд: {self.game.current_position}"

        self.page.update()

    def reset(self, e):
        self.game.reset()

        self.ui.status.value = "Нажми выстрел"
        self.ui.status.color = "black"

        self.ui.lives.value = "❤️ ❤️ ❤️"
        self.ui.round.value = "Раунд: 1"

        self.page.update()