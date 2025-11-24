import tkinter as tk
from tkinter import PhotoImage, Label
import pygame
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(folder, file):
    return os.path.join(BASE_DIR, folder, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def show_image(root, img_path):
    img = PhotoImage(file=img_path)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(pady=10)

def create_app():
    root = tk.Tk()
    root.title("Мемы из Интернета")
    root.geometry("450x600")
    root.resizable(False, False)

    tk.Label(root, text="Нажми кнопку для мема!", font=("Arial", 18)).pack(pady=20)

    tk.Button(
        root, text="Мем 1", font=("Arial", 15),
        command=lambda: [
            play_sound(abs_path("sounds", "ba-ba-ba-banana-minion.mp3")),
            show_image(root, abs_path("images", "minions-6266993_1280.png"))
        ]
    ).pack(pady=8)

    root.mainloop()

create_app()
