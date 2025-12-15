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

display = tk.Text(...)
display.tag_configure("title", ...)
display.tag_configure("desc", ...)

def show_movies(random_pick=False):
    # Shows movies based on selected genre
    genre = genre_var.get()
    if genre not in movies:
        messagebox.showwarning("Error", "Please select a genre.")
        return

    display.delete(1.0, tk.END)

    # Choose either random movies or all movies
    picks = random.sample(movies[genre], 3) if random_pick else movies[genre]

    display.insert(tk.END, f"{genre_emojis[genre]} {genre} Movies\n\n", "title")

    for m in picks:
        display.insert(tk.END, m["title"] + "\n", "title")
        display.insert(tk.END, m["desc"] + "\n\n", "desc")

    status_label.config(text="Surprise picks loaded!" if random_pick else f"{len(movies[genre])} movies loaded.")

def reset_ui():
    # Clears selections and text display
    genre_var.set("Choose a genre")
    display.delete(1.0, tk.END)
    status_label.config(text="")
   