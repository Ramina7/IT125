import flet as ft


class UI:
    def __init__(self):
        self.title = ft.Text("Русская рулетка", size=26, weight="bold")

        self.revolver = ft.Image(
            src="revolver.png",  
            width=150,
            height=150
        )

        self.status = ft.Text("Нажми выстрел", size=20)

        self.lives = ft.Text("❤️ ❤️ ❤️", size=20)

        self.round = ft.Text("Раунд: 1")

        self.shoot_btn = ft.ElevatedButton("🔫 Выстрел")
        self.reset_btn = ft.ElevatedButton("🔄 Перезарядка")

        self.sound = ft.Audio(src="sound.mp3")

    def build(self):
        return [
            self.title,
            self.revolver,
            self.status,
            self.lives,
            self.round,
            self.shoot_btn,
            self.reset_btn,
            self.sound
        ]