import tkinter as tk
from tkinter import font, messagebox
import random

movies = { ... }

root = tk.Tk()
root.title("Popcorn Picks")
root.geometry("720x780")
root.configure(bg="#2E2E2E")

title_font = font.Font(size=26, weight="bold")
body_font = font.Font(size=12)
button_font = font.Font(size=11, weight="bold")

