import flet as ft
from app import RouletteApp


def main(page: ft.Page):
    RouletteApp(page)


ft.app(target=main)