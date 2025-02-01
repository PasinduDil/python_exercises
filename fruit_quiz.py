# Name: [Your Name]
# Student Number: [Your Student Number]

import tkinter as tk
import tkinter.messagebox as messagebox
import random
import json

class ProgramGUI:
    def __init__(self):
        # Load or initialize data from "data.txt".
        try:
            with open("data.txt", "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Missing/Invalid file")
            return

        if len(self.data) < 2:
            messagebox.showerror("Error", "Not enough fruit data for the quiz.")
            return

        self.components = ["energy", "fibre", "sugar", "potassium"]
        self.questions_answered = 0
        self.correct_answers = 0

        # Create the main window.
        self.root = tk.Tk()
        self.root.title("Fruit Quiz")

        # Create GUI elements.
        self.label = tk.Label(self.root, text="", font=("Arial", 16))
        self.label.pack(pady=20)

        self.left_button = tk.Button(self.root, text="Left", command=lambda: self.check_answer("left"))
        self.left_button.pack(side=tk.LEFT, padx=20)

        self.right_button = tk.Button(self.root, text="Right", command=lambda: self.check_answer("right"))
        self.right_button.pack(side=tk.RIGHT, padx=20)

        # Show the first question.
        self.show_question()

        # Start the main loop.
        self.root.mainloop()

    def show_question(self):
        # Randomly select two fruits and a nutritional component.
        self.fruits = random.sample(self.data, 2)
        self.component = random.choice(self.components)

        # Update the label with the question.
        self.label.config(text=f"Which fruit has more {self.component}?\n\n"
                               f"Left: {self.fruits[0]['name']} | Right: {self.fruits[1]['name']}")

    def check_answer(self, choice):
        # Determine which fruit has more of the selected component.
        left_value = self.fruits[0][self.component]
        right_value = self.fruits[1][self.component]
        correct_choice = "left" if left_value >= right_value else "right"

        # Check if the user's choice is correct.
        self.questions_answered += 1
        if choice == correct_choice:
            self.correct_answers += 1
            result = "Correct!"
        else:
            result = "Wrong!"

        # Display the result in a message box.
        score = f"Score: {self.correct_answers}/{self.questions_answered}"
        percentage = round((self.correct_answers / self.questions_answered) * 100)
        messagebox.showinfo("Result", f"{result}\n{score} ({percentage}%)")

        # Show the next question.
        self.show_question()


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()