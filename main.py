import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random
import time

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Playground")
        self.root.geometry("700x500")
        
        self.main_menu = ctk.CTkFrame(self.root)
        self.main_menu.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.title_label = ctk.CTkLabel(self.main_menu, text="Python Playground", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.subtitle_label = ctk.CTkLabel(self.main_menu, text="Select a game to play", font=("Arial", 16))
        self.subtitle_label.pack(pady=10)

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

        self.btn_number_guess = ctk.CTkButton(self.main_menu, text="Number Guessing Game", command=self.start_number_guess)
        self.btn_number_guess.pack(pady=5)

        self.btn_tictactoe = ctk.CTkButton(self.main_menu, text="Tic-Tac-Toe", command=self.start_tictactoe)
        self.btn_tictactoe.pack(pady=5)

        self.btn_memory_game = ctk.CTkButton(self.main_menu, text="Memory Card Game", command=self.start_memory_game)
        self.btn_memory_game.pack(pady=5)

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

    def start_number_guess(self):
        self.clear_frame()
        NumberGuessingGame(self.root, self)

    def start_tictactoe(self):
        self.clear_frame()
        TicTacToe(self.root, self)

    def start_memory_game(self):
        self.clear_frame()
        MemoryCardGame(self.root, self)


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
        ]
        self.current_sentence = ""
        self.start_time = None
        self.score = 0

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Typing Speed Game", font=("Arial", 18))
        self.label.pack(pady=10)

        self.sentence_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 14), wraplength=550)
        self.sentence_label.pack(pady=10)

        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Type the sentence here", width=500)
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
        self.sentence_label.configure(text=f"{self.current_sentence}")
        self.entry.delete(0, tk.END)
        self.start_time = time.time()

    def check_word(self, event=None):
        typed_word = self.entry.get()
        time_taken = time.time() - self.start_time
        
        if typed_word == self.current_sentence:
            self.status_label.configure(text=f"Correct! Time: {time_taken:.2f}s", fg_color="green")
            self.score += max(10 - int(time_taken), 1)
        else:
            self.status_label.configure(text=f"Some mistakes! Time: {time_taken:.2f}s. Try again!", fg_color="red")

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
        self.attempts = 3
        self.status_label.configure(text=f"Attempts left: {self.attempts}", fg_color="transparent")
        self.submit_button.configure(state=tk.NORMAL)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        if guess == self.word:
            self.status_label.configure(text="Correct! Well done!", fg_color="green")
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")
            self.root.after(1000, self.new_word)
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


class NumberGuessingGame:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.min_number = 1
        self.max_number = 100
        self.max_attempts = 7

        self.secret_number = None
        self.attempts_left = self.max_attempts
        self.score = 0

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.frame, text="Number Guessing Game", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.instruction_label = ctk.CTkLabel(
            self.frame,
            text=f"Guess a number between {self.min_number} and {self.max_number}.",
            font=("Arial", 14),
            wraplength=500
        )
        self.instruction_label.pack(pady=10)

        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Enter your guess")
        self.entry.pack(pady=5)

        self.submit_button = ctk.CTkButton(self.frame, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.score_label = ctk.CTkLabel(self.frame, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(pady=10)

        self.new_round()

    def new_round(self):
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts_left = self.max_attempts
        self.status_label.configure(
            text=f"New round started! Attempts left: {self.attempts_left}",
            fg_color="transparent"
        )
        self.entry.delete(0, tk.END)

    def check_guess(self):
        guess_text = self.entry.get().strip()

        if not guess_text.isdigit():
            self.status_label.configure(text="Please enter a valid number.", fg_color="red")
            return

        guess = int(guess_text)

        if guess < self.min_number or guess > self.max_number:
            self.status_label.configure(
                text=f"Number must be between {self.min_number} and {self.max_number}.",
                fg_color="red"
            )
            return

        self.attempts_left -= 1

        if guess == self.secret_number:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")
            self.status_label.configure(
                text=f"Correct! The number was {self.secret_number}. Starting a new round...",
                fg_color="green"
            )
            self.root.after(1500, self.new_round)
        else:
            if guess < self.secret_number:
                hint = "Too low!"
            else:
                hint = "Too high!"

            if self.attempts_left > 0:
                self.status_label.configure(
                    text=f"{hint} Attempts left: {self.attempts_left}",
                    fg_color="red"
                )
            else:
                self.status_label.configure(
                    text=f"Out of attempts! The number was {self.secret_number}.",
                    fg_color="red"
                )
                self.root.after(1500, self.new_round)

        self.entry.delete(0, tk.END)

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)


class TicTacToe:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.frame, text="Tic-Tac-Toe", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.info_label = ctk.CTkLabel(
            self.frame,
            text="You are X, Computer is O.\nClick a square to play.",
            font=("Arial", 14)
        )
        self.info_label.pack(pady=5)

        self.grid_frame = ctk.CTkFrame(self.frame)
        self.grid_frame.pack(pady=10)

        self.buttons = []
        for i in range(9):
            btn = ctk.CTkButton(
                self.grid_frame,
                text="",
                width=80,
                height=80,
                font=("Arial", 24),
                command=lambda idx=i: self.handle_click(idx)
            )
            row, col = divmod(i, 3)
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

        self.status_label = ctk.CTkLabel(self.frame, text="Your turn (X)", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.buttons_bottom_frame = ctk.CTkFrame(self.frame)
        self.buttons_bottom_frame.pack(pady=10)

        self.restart_button = ctk.CTkButton(self.buttons_bottom_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(side=tk.LEFT, padx=5)

        self.back_button = ctk.CTkButton(self.buttons_bottom_frame, text="Back to Menu", command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=5)

    def handle_click(self, index):
        if self.game_over or self.board[index] != "":
            return

        self.board[index] = "X"
        self.buttons[index].configure(text="X")
        winner = self.check_winner()

        if winner:
            self.end_game(winner)
            return

        self.status_label.configure(text="Computer's turn (O)")
        self.root.after(400, self.computer_move)

    def computer_move(self):
        if self.game_over:
            return

        empty_indices = [i for i, v in enumerate(self.board) if v == ""]
        if not empty_indices:
            return

        choice = random.choice(empty_indices)
        self.board[choice] = "O"
        self.buttons[choice].configure(text="O")

        winner = self.check_winner()
        if winner:
            self.end_game(winner)
        else:
            self.status_label.configure(text="Your turn (X)")

    def check_winner(self):
        winning_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in winning_combos:
            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if "" not in self.board:
            return "Tie"

        return None

    def end_game(self, winner):
        self.game_over = True
        if winner == "Tie":
            self.status_label.configure(text="It's a tie!")
        elif winner == "X":
            self.status_label.configure(text="You win!")
        else:
            self.status_label.configure(text="Computer wins!")

    def restart_game(self):
        self.board = [""] * 9
        self.game_over = False
        for btn in self.buttons:
            btn.configure(text="")
        self.current_player = "X"
        self.status_label.configure(text="Your turn (X)")

    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)


class MemoryCardGame:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        
        
        self.grid_size = 4  
        self.total_cards = self.grid_size * self.grid_size
        
        
        self.symbols = ["🍎", "🍊", "🍋", "🍇", "🍓", "🍒", "🥝", "🍑", 
                        "⭐", "🌙", "☀️", "🌈", "❤️", "💎", "🎵", "🎮"]
        
        
        self.cards = []
        self.card_buttons = []
        self.first_card = None
        self.second_card = None
        self.matches_found = 0
        self.moves = 0
        self.can_click = True
        self.game_started = False
        self.start_time = None
        
        self.setup_ui()
        self.setup_game()
    
    def setup_ui(self):
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        
        self.title_label = ctk.CTkLabel(self.frame, text="Memory Card Game", font=("Arial", 22, "bold"))
        self.title_label.pack(pady=10)
        
        
        self.info_label = ctk.CTkLabel(
            self.frame,
            text="Find all matching pairs! Click on cards to reveal them.",
            font=("Arial", 14)
        )
        self.info_label.pack(pady=5)
        
        
        self.stats_frame = ctk.CTkFrame(self.frame)
        self.stats_frame.pack(pady=10)
        
        self.moves_label = ctk.CTkLabel(self.stats_frame, text="Moves: 0", font=("Arial", 14))
        self.moves_label.pack(side=tk.LEFT, padx=20)
        
        self.pairs_label = ctk.CTkLabel(self.stats_frame, text="Pairs: 0/8", font=("Arial", 14))
        self.pairs_label.pack(side=tk.LEFT, padx=20)
        
        self.timer_label = ctk.CTkLabel(self.stats_frame, text="Time: 0s", font=("Arial", 14))
        self.timer_label.pack(side=tk.LEFT, padx=20)
        
        
        self.grid_frame = ctk.CTkFrame(self.frame)
        self.grid_frame.pack(pady=15)
        
        
        self.status_label = ctk.CTkLabel(self.frame, text="Click any card to start!", font=("Arial", 14))
        self.status_label.pack(pady=10)
        
        
        self.buttons_frame = ctk.CTkFrame(self.frame)
        self.buttons_frame.pack(pady=10)
        
        self.restart_button = ctk.CTkButton(
            self.buttons_frame, 
            text="New Game", 
            command=self.restart_game,
            width=120
        )
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
        self.back_button = ctk.CTkButton(
            self.buttons_frame, 
            text="Back to Menu", 
            command=self.go_back,
            width=120
        )
        self.back_button.pack(side=tk.LEFT, padx=10)
    
    def setup_game(self):
        
        for btn in self.card_buttons:
            btn.destroy()
        self.card_buttons = []
        
        
        self.first_card = None
        self.second_card = None
        self.matches_found = 0
        self.moves = 0
        self.can_click = True
        self.game_started = False
        self.start_time = None
        
        
        num_pairs = self.total_cards // 2
        selected_symbols = self.symbols[:num_pairs]
        self.cards = selected_symbols * 2  
        random.shuffle(self.cards)
        
        
        for i in range(self.total_cards):
            btn = ctk.CTkButton(
                self.grid_frame,
                text="?",
                width=70,
                height=70,
                font=("Arial", 28),
                fg_color="#4a4a4a",
                hover_color="#5a5a5a",
                command=lambda idx=i: self.card_clicked(idx)
            )
            row, col = divmod(i, self.grid_size)
            btn.grid(row=row, column=col, padx=4, pady=4)
            self.card_buttons.append(btn)
        
        
        self.moves_label.configure(text="Moves: 0")
        self.pairs_label.configure(text=f"Pairs: 0/{num_pairs}")
        self.timer_label.configure(text="Time: 0s")
        self.status_label.configure(text="Click any card to start!")
    
    def card_clicked(self, index):
        if not self.can_click:
            return
        
        
        if not self.game_started:
            self.game_started = True
            self.start_time = time.time()
            self.update_timer()
            self.status_label.configure(text="Find the matching pairs!")
        
        
        button = self.card_buttons[index]
        if button.cget("state") == "disabled" or button.cget("text") != "?":
            return
        
        
        symbol = self.cards[index]
        button.configure(text=symbol, fg_color="#2d5a27", hover_color="#2d5a27")
        
        if self.first_card is None:
            
            self.first_card = index
        else:
            
            self.second_card = index
            self.moves += 1
            self.moves_label.configure(text=f"Moves: {self.moves}")
            
            
            self.can_click = False
            self.root.after(600, self.check_match)
    
    def check_match(self):
        first_symbol = self.cards[self.first_card]
        second_symbol = self.cards[self.second_card]
        
        if first_symbol == second_symbol:
            
            self.matches_found += 1
            num_pairs = self.total_cards // 2
            self.pairs_label.configure(text=f"Pairs: {self.matches_found}/{num_pairs}")
            
            
            self.card_buttons[self.first_card].configure(
                state="disabled", 
                fg_color="#1a5a1a",
                text_color_disabled="white"
            )
            self.card_buttons[self.second_card].configure(
                state="disabled", 
                fg_color="#1a5a1a",
                text_color_disabled="white"
            )
            
            self.status_label.configure(text="Match found! 🎉", fg_color="green")
            
            
            if self.matches_found == num_pairs:
                self.game_won()
        else:
            
            self.card_buttons[self.first_card].configure(
                text="?", 
                fg_color="#4a4a4a",
                hover_color="#5a5a5a"
            )
            self.card_buttons[self.second_card].configure(
                text="?", 
                fg_color="#4a4a4a",
                hover_color="#5a5a5a"
            )
            self.status_label.configure(text="No match. Try again!", fg_color="red")
        
        
        self.first_card = None
        self.second_card = None
        self.can_click = True
        
        
        self.root.after(1000, lambda: self.status_label.configure(fg_color="transparent"))
    
    def game_won(self):
        elapsed_time = int(time.time() - self.start_time)
        self.status_label.configure(
            text=f"🏆 Congratulations! You won in {self.moves} moves and {elapsed_time}s! 🏆",
            fg_color="green"
        )
        self.can_click = False
    
    def update_timer(self):
        if self.game_started and self.matches_found < self.total_cards // 2:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.configure(text=f"Time: {elapsed}s")
            self.root.after(1000, self.update_timer)
    
    def restart_game(self):
        self.setup_game()
    
    def go_back(self):
        self.frame.destroy()
        self.app.__init__(self.root)


if __name__ == "__main__":
    root = ctk.CTk()
    app = GameApp(root)
    root.mainloop()
