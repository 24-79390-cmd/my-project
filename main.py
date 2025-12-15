import tkinter as tk
from tkinter import font, messagebox
import random

# ---------------- MOVIE DATA ---------------- #
# This dictionary stores all movies grouped by genre.
# Each movie has a title and a short description.

movies = {
    "Action": [
        {"title": "Mad Max: Fury Road", "desc": "In a post-apocalyptic wasteland, Max teams up with Furiosa to escape a tyrant warlord. The film is driven by nonstop vehicular combat across the desert. It focuses on survival, freedom, and rebellion."},
        {"title": "John Wick", "desc": "A retired hitman is pulled back into the criminal underworld after a personal tragedy. His journey is marked by precise and relentless combat. The story centers on revenge and consequences."},
        {"title": "Die Hard", "desc": "A police officer is trapped in a skyscraper overtaken by terrorists. Using wit and determination, he fights to save hostages. The film highlights courage under extreme pressure."},
        {"title": "The Dark Knight", "desc": "Batman faces the Joker, a criminal mastermind who thrives on chaos. Their conflict challenges moral boundaries. The film explores justice and sacrifice."},
        {"title": "Avengers: Endgame", "desc": "The Avengers reunite after a devastating defeat. They attempt a risky plan to reverse the damage caused by Thanos. The film emphasizes teamwork, loss, and hope."},
        {"title": "Gladiator", "desc": "A Roman general is betrayed and sold into slavery. He rises as a gladiator seeking revenge. Honor and justice guide his path."},
        {"title": "Inception", "desc": "A skilled thief enters dreams to steal information. He is tasked with planting an idea instead. Reality and imagination blur throughout the mission."},
        {"title": "The Matrix", "desc": "A hacker discovers the world is a simulated reality. He joins a rebellion against machines. The film questions freedom and identity."},
        {"title": "Fast & Furious", "desc": "Street racers become involved in dangerous criminal operations. Loyalty and family bonds drive their actions. High-speed action defines the film."},
        {"title": "Mission: Impossible", "desc": "An elite agent takes on impossible espionage missions. Each assignment requires precision and sacrifice. Trust is constantly tested."},
        {"title": "Black Panther", "desc": "T’Challa becomes king of Wakanda after his father’s death. He must protect his nation from internal and external threats. Leadership and responsibility are central themes."},
        {"title": "Wonder Woman", "desc": "An Amazon warrior leaves her homeland to stop a world war. She discovers humanity’s strengths and flaws. Compassion guides her strength."},
        {"title": "Logan", "desc": "An aging Wolverine protects a young mutant. His powers are fading as danger increases. The story explores legacy and sacrifice."},
        {"title": "Guardians of the Galaxy", "desc": "A group of criminals unite to stop a cosmic threat. Their teamwork grows through conflict. Humor balances the action."},
        {"title": "Captain America: The Winter Soldier", "desc": "Captain America uncovers a conspiracy within a global organization. He faces a mysterious assassin. Loyalty and truth are tested."}
    ],

    "Comedy": [
        {"title": "The Hangover", "desc": "Three friends wake up after a bachelor party with no memory of the night before. They search Las Vegas for their missing friend. Chaos fuels the humor."},
        {"title": "Superbad", "desc": "Two high school seniors try to enjoy one last party. Their plans repeatedly go wrong. Friendship anchors the comedy."},
        {"title": "Groundhog Day", "desc": "A man relives the same day repeatedly. Over time, he changes himself. The film focuses on growth and redemption."},
        {"title": "Airplane!", "desc": "A former pilot must land a plane during an emergency. The movie uses nonstop visual jokes. It parodies disaster films."},
        {"title": "Monty Python and the Holy Grail", "desc": "King Arthur searches for the Holy Grail. Absurd humor replaces logic. The film satirizes medieval legends."},
        {"title": "Shaun of the Dead", "desc": "A man tries to fix his life during a zombie outbreak. Comedy and horror blend together. Relationships drive the story."},
        {"title": "The Big Lebowski", "desc": "A laid-back man is mistaken for someone else. He becomes involved in crime by accident. Humor comes from confusion."},
        {"title": "Ferris Bueller's Day Off", "desc": "A student skips school for a day of fun. He outsmarts authority figures. The film celebrates youth."},
        {"title": "Ghostbusters", "desc": "Scientists start a business capturing ghosts. Their work escalates into a city-wide threat. Comedy meets fantasy."},
        {"title": "Anchorman", "desc": "A news anchor struggles with competition. His ego causes chaos. The film mocks media culture."},
        {"title": "Dumb and Dumber", "desc": "Two unintelligent friends travel cross-country. Their mistakes create constant trouble. Absurdity defines the humor."},
        {"title": "The Princess Bride", "desc": "A young man rescues his true love. Adventure and romance mix with humor. The story is lighthearted."},
        {"title": "Office Space", "desc": "Office workers rebel against corporate life. Small actions spiral into chaos. The film reflects workplace frustration."},
        {"title": "Zoolander", "desc": "A fashion model is involved in a conspiracy. His lack of intelligence complicates everything. The industry is heavily satirized."},
        {"title": "The Grand Budapest Hotel", "desc": "A concierge and his protégé face political chaos. Their bond drives the story. The film blends humor and nostalgia."}
    ],

    "Drama": [
        {"title": "The Shawshank Redemption", "desc": "A man is sentenced to life in prison. He maintains hope through friendship. Redemption unfolds over decades."},
        {"title": "Forrest Gump", "desc": "A simple man lives through historic events. His kindness influences others. The film highlights destiny."},
        {"title": "The Godfather", "desc": "A crime family rises to power. Loyalty and betrayal shape their fate. Authority comes at a cost."},
        {"title": "Schindler's List", "desc": "A businessman saves Jewish lives during the Holocaust. His moral transformation drives the story. Humanity shines amid horror."},
        {"title": "Titanic", "desc": "Two lovers meet aboard a doomed ship. Class differences divide them. Tragedy seals their fate."},
        {"title": "The Green Mile", "desc": "Prison guards encounter a man with miraculous abilities. Justice and compassion collide. The story is deeply emotional."},
        {"title": "Fight Club", "desc": "A man forms an underground fight club. Identity and consumerism are questioned. Chaos escalates."},
        {"title": "A Beautiful Mind", "desc": "A brilliant mathematician battles mental illness. His struggle affects relationships. Triumph comes through perseverance."},
        {"title": "The King's Speech", "desc": "A king struggles with a speech disorder. Therapy helps him lead his nation. Confidence is earned."},
        {"title": "Spotlight", "desc": "Journalists uncover institutional abuse. Truth is pursued despite resistance. Integrity drives the investigation."},
        {"title": "Moonlight", "desc": "A boy grows up facing identity struggles. Each stage shapes his character. The film explores self-acceptance."},
        {"title": "The Social Network", "desc": "A student creates a global social platform. Success breeds conflict. Ambition shapes relationships."},
        {"title": "Argo", "desc": "A CIA agent plans a daring rescue. A fake movie production becomes the cover. Tension builds steadily."},
        {"title": "The Revenant", "desc": "A frontiersman survives brutal wilderness conditions. Revenge motivates his journey. Nature is a constant threat."},
        {"title": "Pulp Fiction", "desc": "Crime stories intersect in unexpected ways. Nonlinear storytelling defines the film. Dialogue drives tension."}
    ],

    "Horror": [
        {"title": "The Shining", "desc": "A family stays in an isolated hotel. Supernatural forces affect the father. Madness slowly takes over."},
        {"title": "Psycho", "desc": "A woman checks into a quiet motel. Dark secrets emerge. Suspense builds through psychological horror."},
        {"title": "Get Out", "desc": "A man visits his girlfriend’s family. He uncovers a disturbing secret. Social commentary fuels the horror."},
        {"title": "Hereditary", "desc": "A family experiences a series of tragedies. Dark forces influence their fate. Grief drives the terror."},
        {"title": "The Conjuring", "desc": "Paranormal investigators face a haunted house. A family is terrorized by demons. Faith plays a key role."},
        {"title": "It", "desc": "Children face an evil entity. Fear feeds the monster. Friendship gives strength."},
        {"title": "The Exorcist", "desc": "A young girl becomes possessed. Priests attempt an exorcism. Faith is severely tested."},
        {"title": "Halloween", "desc": "A masked killer returns home. He stalks victims on Halloween night. Fear is relentless."},
        {"title": "Scream", "desc": "Teens are targeted by a masked killer. Horror rules are referenced. Mystery drives the plot."},
        {"title": "The Babadook", "desc": "A mother struggles with grief. A sinister presence grows stronger. Psychological horror dominates."},
        {"title": "Us", "desc": "A family encounters their doppelgängers. Violence erupts suddenly. Identity is questioned."},
        {"title": "A Quiet Place", "desc": "Creatures hunt by sound. A family must stay silent. Survival depends on communication."},
        {"title": "Sinister", "desc": "A writer finds disturbing home videos. Each discovery worsens the danger. Evil repeats itself."},
        {"title": "The Witch", "desc": "A family lives in isolation. Superstition grows into terror. Faith and fear collide."},
        {"title": "Midsommar", "desc": "Friends attend a strange festival. Traditions become violent. Daylight intensifies the horror."}
    ],

    "Sci-Fi": [
        {"title": "Interstellar", "desc": "Explorers travel through space to save humanity. Time behaves differently near black holes. Love transcends dimensions."},
        {"title": "The Martian", "desc": "An astronaut is stranded on Mars. Science keeps him alive. Survival becomes a global mission."},
        {"title": "Arrival", "desc": "Linguists communicate with aliens. Language alters perception of time. Understanding becomes crucial."},
        {"title": "Dune", "desc": "A noble family controls a desert planet. Power struggles dominate. Destiny shapes leadership."},
        {"title": "Ex Machina", "desc": "A programmer tests an advanced AI. Manipulation unfolds quietly. Consciousness is questioned."},
        {"title": "Blade Runner 2049", "desc": "A replicant uncovers a hidden truth. Society blurs humanity and machines. Identity drives the story."},
        {"title": "Gravity", "desc": "Astronauts are stranded in space. Survival depends on resilience. Isolation dominates the experience."},
        {"title": "Edge of Tomorrow", "desc": "A soldier relives the same battle. Each death teaches survival. Time resets constantly."},
        {"title": "Her", "desc": "A man falls in love with an AI. Emotional connection grows digitally. Loneliness defines the theme."},
        {"title": "Snowpiercer", "desc": "Humanity survives on a moving train. Class divisions spark rebellion. Control fuels conflict."},
        {"title": "The Fifth Element", "desc": "A cab driver helps save the world. Ancient forces awaken. Action blends with humor."},
        {"title": "Contact", "desc": "A scientist discovers alien signals. Faith and science clash. Humanity reaches outward."},
        {"title": "Eternal Sunshine of the Spotless Mind", "desc": "A couple erases memories of each other. Love resurfaces unexpectedly. Memory defines identity."},
        {"title": "Minority Report", "desc": "Crimes are predicted before happening. A detective is accused of future murder. Free will is questioned."},
        {"title": "District 9", "desc": "Aliens are confined to slums. Human prejudice is exposed. Transformation drives empathy."}
    ]
}


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

# ---------------- START THE APP ---------------- #
# Keeps the window running until the user exits

root.mainloop()


   