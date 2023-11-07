import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Loop through each letter in the word and update word_guessed
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)

    def run_game(self):
        while self.num_lives > 0 and self.num_letters > 0:
            print("Word Guessed:", " ".join(self.word_guessed))
            print("Number of Lives:", self.num_lives)
            print("List of Guesses:", self.list_of_guesses)
            self.ask_for_input()
            if "_" not in self.word_guessed:
                print("Congratulations! You guessed the word:", self.word)
                break
            self.num_lives -= 1

# Example usage:
word_list = ["apple", "banana", "cherry", "grape", "watermelon"]
hangman_game = Hangman(word_list)
hangman_game.run_game()

