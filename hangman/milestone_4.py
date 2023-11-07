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
        # Step 1: Define the check_guess method
        guess = guess.lower()

        if guess in self.word:
            # In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
            print(f"Good guess! {guess} is in the word.")
        # You can continue with the logic of this method in the next task.

    def ask_for_input(self):
        # Step 2: Define the ask_for_input method
        while True:
            guess = input("Guess a letter: ")

            if not (len(guess) == 1 and guess.isalpha()):
                # If the guess is NOT a single alphabetical character
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                # If the guess is already in the list_of_guesses
                print("You already tried that letter!")
            else:
                # If the guess is a single alphabetical character and not already in list_of_guesses
                self.check_guess(guess)  # Call the check_guess method
                self.list_of_guesses.append(guess)  # Append the guess to the list_of_guesses

    # Step 3: Call the ask_for_input method to test your code.
    def run_game(self):
        self.ask_for_input()

# Example usage:
word_list = ["apple", "banana", "cherry", "grape", "watermelon"]
hangman_game = Hangman(word_list)
hangman_game.run_game()
