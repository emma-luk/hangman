import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.remaining_letters = len(set(self.word))
        self.guesses = []

    def _display_game_state(self):
        print("Word Guessed:", " ".join(self.word_guessed))
        print("Number of Lives:", self.num_lives)
        print("List of Guesses:", self.guesses)

    def handle_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.remaining_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        self.guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.guesses:
                print("You already tried that letter!")
            else:
                self.handle_guess(guess)

    def play_game(self):
        while True:
            if self.num_lives == 0:
                print('You lost!')
                break
            elif self.remaining_letters > 0:
                self.ask_for_input()
            else:
                print('Congratulations. You won the game!')
                break

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "grape", "watermelon"]
    game = Hangman(word_list)
    game.play_game()

