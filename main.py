import tkinter as tk
from tkinter import font, messagebox
import random

movies = { ... }

# ---------------- UI SETUP ---------------- #
# This section creates the main window and basic styles.

root = tk.Tk()
root.title("Popcorn Picks")
root.geometry("720x780")
root.configure(bg="#2E2E2E")

# Fonts used in the app
title_font = font.Font(size=26, weight="bold")
body_font = font.Font(size=12)
button_font = font.Font(size=11, weight="bold")

# App title label
tk.Label(root, text="🍿 Popcorn Picks", font=title_font, bg="#2E2E2E", fg="#FFD700").pack(pady=20)

# Label used to show status messages
status_label = tk.Label(root, text="", font=body_font, bg="#2E2E2E", fg="white")
status_label.pack()

# Dropdown menu for selecting genre
genre_var = tk.StringVar(value="Choose a genre")
tk.OptionMenu(root, genre_var, *movies.keys()).pack(pady=10)
