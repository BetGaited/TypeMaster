import random

def main(page: ft.Page):
    words = ["Sonic", "Shadow", "Silver", "Amy", "Knuckles", "Tails", "Blaze", "Rouge", "Omega", "Cream", "Vector", "Espio",
            "Charmy", "Eggman", "Metal"]
    random.shuffle(words)
    words = words[:15]

    current_index = 0
    mistakes = 0