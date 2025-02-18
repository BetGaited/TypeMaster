import flet as ft
import random

def main(page: ft.Page):
    words = ["Sonic", "Shadow", "Silver", "Amy", "Knuckles", "Tails", "Blaze", "Rouge", "Omega", "Cream", "Vector", "Espio",
            "Charmy", "Eggman", "Metal"]
    random.shuffle(words)
    words = words[:15]

    current_index = 0
    mistakes = 0

    word_display = ft.Text(words[current_index], size=24, weight=ft.FontWeight.BOLD)
    status_label = ft.Text("", size=20)
    progress_label = ft.Text(f"Progress: {current_index + 1}/{len(words)}", size=16)
    accuracy_label = ft.Text("Accuracy: 100%", size=16)
    input_field = ft.TextField(label="Type the word here", on_submit=lambda e: check_word(e, page))

    def check_word(event, page):
        nonlocal current_index, mistakes
        user_input = input_field.value.strip()

        if user_input.lower() == words[current_index].lower():
                status_label.value = "Correct!"
                status_label.color = "green"
        else:
                status_label.value = "Incorrect!"
                status_label.color = "red"
                mistakes += 1

        current_index += 1
        if current_index < len(words):
                word_display.value = words[current_index]
                progress_label.value = f"Progress: {current_index + 1}/{len(words)}"
        else:
            accuracy = ((len(words) - mistakes) / len(words)) * 100
            accuracy_label.value = f"Accuracy: {accuracy:.2f}%"
            input_field.disabled = True
            status_label.value = "Game Over!"

ft.app(target=main)