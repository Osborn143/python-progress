import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def _init_(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.level = tk.StringVar()
        self.number = 0
        self.max_guesses = 0
        self.num_guesses = 0
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select level:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        tk.Radiobutton(self.master, text="Easy", variable=self.level, value="easy").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        tk.Radiobutton(self.master, text="Medium", variable=self.level, value="medium").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        tk.Radiobutton(self.master, text="Hard", variable=self.level, value="hard").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        tk.Button(self.master, text="Start", command=self.start_game).grid(row=4, column=0, padx=10, pady=10)

        self.guess_entry = tk.Entry(self.master, width=10)
        self.guess_entry.grid(row=5, column=0, padx=10, pady=10)

        tk.Button(self.master, text="Guess", command=self.check_guess).grid(row=6, column=0, padx=10, pady=10)

        self.message_label = tk.Label(self.master, text="")
        self.message_label.grid(row=7, column=0, padx=10, pady=10)

    def start_game(self):
        level = self.level.get()
        if level == "easy":
            self.number = random.randint(1, 10)
            self.max_guesses = 3
        elif level == "medium":
            self.number = random.randint(1, 50)
            self.max_guesses = 5
        else: # level == "hard"
            self.number = random.randint(1, 100)
            self.max_guesses = 7
        self.num_guesses = 0
        self.guess_entry.delete(0, tk.END)
        self.message_label.configure(text=f"I'm thinking of a number between 1 and {self.number}. You have {self.max_guesses} guesses to guess it.")

    def check_guess(self):
        guess_str = self.guess_entry.get()
        if guess_str == "":
            messagebox.showwarning("Error", "Please enter a guess.")
            return
        try:
            guess = int(guess_str)
        except ValueError:
            messagebox.showwarning("Error", "Invalid guess. Please enter an integer.")
            return
        self.num_guesses += 1
        if guess < self.number:
            self.message_label.configure(text="Your guess is too low.")
        elif guess > self.number:
            self.message_label.configure(text="Your guess is too high.")
        else:
            messagebox.showinfo("Congratulations", f"Congratulations! You guessed the number in {self.num_guesses} guesses.")
            self.start_game()
        if self.num_guesses == self.max_guesses:
            messagebox.showwarning("Sorry", f"Sorry, you ran out of guesses. The number was {self.number_guesses} guesses.")