import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialise the attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

# Example usage:
word_list = ["apple", "banana", "cherry", "grape", "watermelon"]
hangman_game = Hangman(word_list)
print("Secret Word:", hangman_game.word)
print("Word Guessed:", hangman_game.word_guessed)
print("Number of Lives:", hangman_game.num_lives)
print("Number of Letters:", hangman_game.num_letters)
print("List of Guesses:", hangman_game.list_of_guesses)
