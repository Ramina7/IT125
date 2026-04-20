import flet as ft
from ui import UI
import smtplib
from email.mime.text import MIMEText


class ProfileApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Анкеты'
        self.page.window_width = 500
        self.page.window_height = 650

        self.ui = UI()

        self.page.overlay.append(self.ui.file_picker)

        self.build_event()
        self.page.add(*self.ui.build())

    def build_event(self):
        self.ui.button.on_click = self.create_profile
        self.ui.age.on_change = self.update_age
        self.ui.theme_btn.on_click = self.toggle_theme
        self.ui.upload_btn.on_click = self.pick_file
        self.ui.file_picker.on_result = self.on_file_selected

    def update_age(self, e):
        self.ui.age_text.value = f'Возраст: {int(self.ui.age.value)}'
        self.page.update()

    def toggle_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

    def pick_file(self, e):
        self.ui.file_picker.pick_files(allow_multiple=False)

    def on_file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.ui.photo.src = e.files[0].path
            self.page.update()

    def send_email(self, text):
        sender = "mashanlo_ra@iuca.kg"
        password = "mashanlo_ra@iuca.kg"
        receiver = "mashanlo_ra@iuca.kg"

        msg = MIMEText(text)
        msg["Subject"] = "Новая анкета"
        msg["From"] = sender
        msg["To"] = receiver

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.send_message(msg)
        except Exception as e:
            print("Ошибка отправки:", e)

    def create_profile(self, e):
        errors = []

        if not self.ui.name.value:
            errors.append("Введите имя")
        if not self.ui.city.value:
            errors.append("Выберите город")
        if not self.ui.level.value:
            errors.append("Выберите уровень")

        if errors:
            self.ui.result.value = "Ошибки:\n" + "\n".join(errors)
            self.ui.result.color = "red"
            self.page.update()
            return

        skills = []
        if self.ui.skill1.value:
            skills.append("Python")
        if self.ui.skill2.value:
            skills.append("Django")
        if self.ui.skill3.value:
            skills.append("Flet")

        self.ui.result.value = (
            f'Имя: {self.ui.name.value}\n'
            f'Город: {self.ui.city.value}\n'
            f'Возраст: {self.ui.age.value}\n'
            f'Навыки: {", ".join(skills)}\n'
            f'Уровень: {self.ui.level.value}\n'
            f'Готов к работе: {"Да" if self.ui.active.value else "Нет"}'
        )

        self.ui.result.color = "green"

        self.send_email(self.ui.result.value)

        self.page.update()