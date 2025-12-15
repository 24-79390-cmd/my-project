import tkinter as tk
from tkinter import font, messagebox
import random

# ---------------- MOVIE DATA ---------------- #
movies = {
    "Action": [
        {"title": "Mad Max: Fury Road", "desc": "In a post-apocalyptic wasteland, Max teams up with Furiosa to escape a tyrant warlord. The film is driven by nonstop vehicular combat across the desert. It focuses on survival, freedom, and rebellion."},
        {"title": "John Wick", "desc": "A retired hitman is pulled back into the criminal underworld after a personal tragedy. His journey is marked by precise and relentless combat. The story centers on revenge and consequences."},
        {"title": "Die Hard", "desc": "A police officer is trapped in a skyscraper overtaken by terrorists. Using wit and determination, he fights to save hostages. The film highlights courage under extreme pressure."},
        {"title": "The Dark Knight", "desc": "Batman faces the Joker, a criminal mastermind who thrives on chaos. Their conflict challenges moral boundaries. The film explores justice and sacrifice."},
        {"title": "Avengers: Endgame", "desc": "The Avengers reunite after a devastating defeat. They attempt a risky plan to reverse the damage caused by Thanos. The film emphasizes teamwork, loss, and hope."}
    ],

    "Comedy": [
        {"title": "The Hangover", "desc": "Three friends wake up after a bachelor party with no memory of the night before. They search Las Vegas for their missing friend. Chaos fuels the humor."},
        {"title": "Superbad", "desc": "Two high school seniors try to enjoy one last party. Their plans repeatedly go wrong. Friendship anchors the comedy."},
        {"title": "Groundhog Day", "desc": "A man relives the same day repeatedly. Over time, he changes himself. The film focuses on growth and redemption."}
    ],

    "Drama": [
        {"title": "The Shawshank Redemption", "desc": "A man is sentenced to life in prison. He maintains hope through friendship. Redemption unfolds over decades."},
        {"title": "Forrest Gump", "desc": "A simple man lives through historic events. His kindness influences others. The film highlights destiny."}
    ],

    "Horror": [
        {"title": "The Shining", "desc": "A family stays in an isolated hotel. Supernatural forces affect the father. Madness slowly takes over."},
        {"title": "Get Out", "desc": "A man visits his girlfriend’s family. He uncovers a disturbing secret. Social commentary fuels the horror."}
    ],

    "Sci-Fi": [
        {"title": "Interstellar", "desc": "Explorers travel through space to save humanity. Time behaves differently near black holes. Love transcends dimensions."},
        {"title": "The Martian", "desc": "An astronaut is stranded on Mars. Science keeps him alive. Survival becomes a global mission."}
    ]
}

# Genre emojis (THIS WAS MISSING)
genre_emojis = {
    "Action": "🔥",
    "Comedy": "😂",
    "Drama": "🎭",
    "Horror": "👻",
    "Sci-Fi": "🚀"
}

# ---------------- UI SETUP ---------------- #
root = tk.Tk()
root.title("Popcorn Picks")
root.geometry("720x780")
root.configure(bg="#2E2E2E")

# Fonts
title_font = font.Font(size=26, weight="bold")
body_font = font.Font(size=12)
button_font = font.Font(size=11, weight="bold")

# Title
tk.Label(
    root,
    text="🍿 Popcorn Picks",
    font=title_font,
    bg="#2E2E2E",
    fg="#FFD700"
).pack(pady=20)

# Status label
status_label = tk.Label(root, text="", font=body_font, bg="#2E2E2E", fg="white")
status_label.pack(pady=5)

# Genre dropdown
genre_var = tk.StringVar(value="Choose a genre")
tk.OptionMenu(root, genre_var, *movies.keys()).pack(pady=10)

# ---------------- TEXT DISPLAY ---------------- #
display = tk.Text(
    root,
    wrap="word",
    height=22,
    width=80,
    bg="#1C1C1C",
    fg="white",
    font=body_font
)
display.pack(padx=10, pady=10)

# Text styles
display.tag_configure("title", font=font.Font(size=14, weight="bold"), foreground="#FFD700")
display.tag_configure("desc", font=body_font, foreground="white")

# ---------------- FUNCTIONS ---------------- #
def show_movies(random_pick=False):
    genre = genre_var.get()

    if genre not in movies:
        messagebox.showwarning("Error", "Please select a genre.")
        return

    display.delete(1.0, tk.END)

    picks = random.sample(movies[genre], min(3, len(movies[genre]))) if random_pick else movies[genre]

    display.insert(tk.END, f"{genre_emojis[genre]} {genre} Movies\n\n", "title")

    for movie in picks:
        display.insert(tk.END, movie["title"] + "\n", "title")
        display.insert(tk.END, movie["desc"] + "\n\n", "desc")

    status_label.config(
        text="Surprise picks loaded!" if random_pick else f"{len(picks)} movies loaded."
    )

def reset_ui():
    genre_var.set("Choose a genre")
    display.delete(1.0, tk.END)
    status_label.config(text="")

# ---------------- BUTTONS ---------------- #
btn_frame = tk.Frame(root, bg="#2E2E2E")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Show Movies",
    font=button_font,
    command=show_movies
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="🎲 Surprise Me",
    font=button_font,
    command=lambda: show_movies(True)
).grid(row=0, column=1, padx=10)

tk.Button(
    btn_frame,
    text="Reset",
    font=button_font,
    command=reset_ui
).grid(row=0, column=2, padx=10)

# ---------------- START APP ---------------- #
root.mainloop()
