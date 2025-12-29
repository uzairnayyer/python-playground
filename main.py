import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random
import time

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Main App Class
class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Playgroundd")
        self.root.geometry("600x400")
        
        # Create main menu frame
        self.main_menu = ctk.CTkFrame(self.root)
        self.main_menu.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.title_label = ctk.CTkLabel(self.main_menu, text="Python Playgroundd", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.title_label = ctk.CTkLabel(self.main_menu, text="Select a game to play", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Buttons for games
        self.btn_guess_word = ctk.CTkButton(self.main_menu, text="Guess the Word", command=self.start_guess_the_word)
        self.btn_guess_word.pack(pady=5)

        self.btn_quiz_game = ctk.CTkButton(self.main_menu, text="Quiz Game", command=self.start_quiz_game)
        self.btn_quiz_game.pack(pady=5)

        self.btn_rps = ctk.CTkButton(self.main_menu, text="Rock, Paper, Scissors", command=self.start_rps)
        self.btn_rps.pack(pady=5)

        self.btn_typing_game = ctk.CTkButton(self.main_menu, text="Typing Speed Game", command=self.start_typing_game)
        self.btn_typing_game.pack(pady=5)

        self.btn_word_scramble = ctk.CTkButton(self.main_menu, text="Word Scramble", command=self.start_word_scramble)
        self.btn_word_scramble.pack(pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_guess_the_word(self):
        self.clear_frame()
        GuessTheWord(self.root, self)

    def start_quiz_game(self):
        self.clear_frame()
        QuizGame(self.root, self)

    def start_rps(self):
        self.clear_frame()
        RockPaperScissors(self.root, self)

    def start_typing_game(self):
        self.clear_frame()
        TypingSpeedGame(self.root, self)

    def start_word_scramble(self):
        self.clear_frame()
        WordScramble(self.root, self)

# Guess the Word Game Class
class GuessTheWord:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.words = [
            "python", "programming", "developer", "keyboard", "software", "algorithm",
            "computer", "debugging", "coding", "function", "mystery", "puzzle", "doodle",
        ]
        self.word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = len(self.word) + 3

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Welcome to Guess the Word!", font=("Arial", 18))
        self.label.pack(pady=10)

        self.word_display = ctk.CTkLabel(self.frame, text=" ".join(self.guessed_word), font=("Arial", 16))
        self.word_display.pack(pady=10)

        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Enter a letter")
        self.entry.pack(pady=5)

        self.submit_button = ctk.CTkButton(self.frame, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.status_label = ctk.CTkLabel(self.frame, text=f"Attempts left: {self.attempts}", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            self.status_label.configure(text="Please enter a single valid letter.")
            return

        if guess in self.guessed_word:
            self.status_label.configure(text="You already guessed that letter.")
            return

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed_word[i] = guess
            self.status_label.configure(text=f"Good job! '{guess}' is in the word.")
        else:
            self.attempts -= 1
            self.status_label.configure(text=f"Wrong guess. You have {self.attempts} attempts left.")

        self.word_display.configure(text=" ".join(self.guessed_word))
        self.entry.delete(0, tk.END)

        if "_" not in self.guessed_word:
            self.status_label.configure(text=f"Congratulations! You guessed the word: {self.word}")
            self.submit_button.configure(state=tk.DISABLED)

        if self.attempts <= 0:
            self.status_label.configure(text=f"Game over! The word was: {self.word}")
            self.submit_button.configure(state=tk.DISABLED)

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)

class QuizGame:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.questions = [
            ("What is the capital of Pakistan?", "islamabad"),
            ("What is the national language of Pakistan?", "urdu"),
            ("Who was the founder of Pakistan?", "quaid-e-azam"),
            ("What is the currency of Pakistan?", "rupee"),
            ("What is the largest city in Pakistan?", "karachi"),
        ]
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.frame, text="Quiz Game", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.question_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 16), wraplength=500)
        self.question_label.pack(pady=10)
        
        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Enter your answer here")
        self.entry.pack(pady=5)

        self.submit_button = ctk.CTkButton(self.frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.score_label = ctk.CTkLabel(self.frame, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question, _ = self.questions[self.current_question_index]
            self.question_label.configure(text=f"Question {self.current_question_index + 1}: {question}")
        else:
            self.question_label.configure(text="Quiz Over!")
            self.submit_button.configure(state=tk.DISABLED)
            self.status_label.configure(text=f"Your final score is: {self.score}")

    def check_answer(self):
        user_answer = self.entry.get().lower().strip()
        _, correct_answer = self.questions[self.current_question_index]

        if user_answer == correct_answer:
            self.score += 1
            self.status_label.configure(text="Correct!", fg_color="green")
        else:
            self.status_label.configure(text=f"Wrong! The correct answer was: {correct_answer}", fg_color="red")

        self.score_label.configure(text=f"Score: {self.score}")
        self.current_question_index += 1
        self.entry.delete(0, tk.END)
        self.display_question()

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)

class RockPaperScissors:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Rock, Paper, Scissors", font=("Arial", 18))
        self.label.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.frame, text="Make your choice!", font=("Arial", 16))
        self.result_label.pack(pady=10)

        self.buttons_frame = ctk.CTkFrame(self.frame)
        self.buttons_frame.pack(pady=10)

        for choice in self.choices:
            button = ctk.CTkButton(self.buttons_frame, text=choice, command=lambda c=choice: self.play(c))
            button.pack(side=tk.LEFT, padx=5)

        self.score_label = ctk.CTkLabel(self.frame, text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_label.configure(text=f"You chose {user_choice}, Computer chose {computer_choice}. {result}")
        self.score_label.configure(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)

class TypingSpeedGame:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.words = [
        "The quick brown fox jumps over the lazy dog in the sunny field by the river.",
        "Python is an easy-to-learn programming language that allows developers to write clean and readable code.",
        "Artificial intelligence is transforming industries and has the potential to improve lives globally.",
        "The weather was beautiful today, with clear skies, a cool breeze, and the sun shining brightly.",
        "A journey of a thousand miles begins with a single step, and each step brings you closer to your goal.",
        "The code was written to function properly, yet there were still several bugs that needed fixing.",
        "Innovation is not just about new ideas, but also about improving on existing systems and making them more efficient.",
        "Reading books is a great way to learn, expand your knowledge, and escape into different worlds of imagination.",
        "Running regularly helps keep the body in good condition and boosts mental health by releasing endorphins.",
        "Technology is evolving rapidly, with breakthroughs happening almost every day in fields like medicine, space, and computing.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Creativity and critical thinking are essential skills in today's fast-paced world, driving progress and innovation.",
        "Learning new languages opens up many opportunities, from travel to professional growth and cultural exchange.",
        "The rain began to fall gently, tapping against the window as the storm moved closer to the town.",
        "Sometimes the best way to solve a problem is to step back, take a deep breath, and think critically.",
        "Working together as a team allows people to combine their strengths and overcome challenges more effectively.",
        "A good plan today is better than a perfect plan tomorrow, as long as it is executed well.",
        "The sun was setting behind the mountains, casting a warm orange glow across the landscape.",
        "Technology has greatly impacted how we communicate, making it easier to connect with people around the world.",
        "The old library was filled with books from floor to ceiling, offering a wealth of knowledge to any reader."
    ]
        self.current_sentence = ""
        self.start_time = None
        self.score = 0

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Typing Speed Game", font=("Arial", 18))
        self.label.pack(pady=10)

        self.sentence_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 16))
        self.sentence_label.pack(pady=10)

        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Type the sentence here")
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_word)

        self.status_label = ctk.CTkLabel(self.frame, text="Press Enter after typing.", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.score_label = ctk.CTkLabel(self.frame, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(pady=10)

        self.new_word()

    def new_word(self):
        self.current_sentence = random.choice(self.words)
        self.sentence_label.configure(text=f"Word: {self.current_sentence}")
        self.entry.delete(0, tk.END)
        self.start_time = time.time()

    def check_word(self, event=None):
        typed_word = self.entry.get()
        if typed_word == self.current_sentence:
            time_taken = time.time() - self.start_time
            self.status_label.configure(text=f"Correct! Time: {time_taken:.2f}s\n", fg_color="green")
            self.score += max(10 - int(time_taken), 1)  # Score based on speed, minimum of 1
        else:
            time_taken = time.time() - self.start_time
            self.score += max(10 - int(time_taken), 1)    
            self.status_label.configure(text=f"Correct! Time: {time_taken:.2f}s\nYou made some mistakes. Try again to improve your speed and accuracy.", fg_color="red")

        self.score_label.configure(text=f"Score: {self.score}")
        self.new_word()

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)

class WordScramble:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.words = [
            "python", "programming", "developer", "keyboard", "software", "algorithm",
            "computer", "debugging", "coding", "function", "mystery", "puzzle", "challenge",
        ]
        self.word = ""
        self.scrambled_word = ""
        self.attempts = 3

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Word Scramble Game", font=("Arial", 18))
        self.label.pack(pady=10)

        self.scrambled_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 16))
        self.scrambled_label.pack(pady=10)

        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Guess the word")
        self.entry.pack(pady=5)

        self.submit_button = ctk.CTkButton(self.frame, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.status_label = ctk.CTkLabel(self.frame, text=f"Attempts left: {self.attempts}", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.score = 0
        self.score_label = ctk.CTkLabel(self.frame, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(pady=10)

        self.new_word()

    def new_word(self):
        self.word = random.choice(self.words)
        self.scrambled_word = "".join(random.sample(self.word, len(self.word)))
        self.scrambled_label.configure(text=f"Scrambled Word: {self.scrambled_word}")
        self.entry.delete(0, tk.END)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        if guess == self.word:
            self.status_label.configure(text="Correct! Well done!", fg_color="green")
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")
            self.new_word()
        else:
            self.attempts -= 1
            self.status_label.configure(text=f"Wrong guess. Attempts left: {self.attempts}", fg_color="red")
            if self.attempts <= 0:
                self.status_label.configure(text=f"Game Over! The word was: {self.word}")
                self.submit_button.configure(state=tk.DISABLED)

        self.entry.delete(0, tk.END)

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)

if __name__ == "__main__":
    root = ctk.CTk()
    app = GameApp(root)
    root.mainloop()

