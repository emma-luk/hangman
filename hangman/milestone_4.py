import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self._initialize_game()

    def _initialize_game(self):
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.remaining_letters = len(set(self.word))
        self.list_of_guesses = []

    def _display_game_state(self):
        print("Word Guessed:", " ".join(self.word_guessed))
        print("Number of Lives:", self.num_lives)
        print("List of Guesses:", self.list_of_guesses)

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
        self.list_of_guesses.append(guess)

    # Other methods...

    def run_game(self):
        while self.num_lives > 0 and self.remaining_letters > 0:
            self._display_game_state()
            self.handle_guess(input("Guess a letter: "))
            if "_" not in self.word_guessed:
                print(f"Congratulations! You guessed the word: {self.word}")
                break
            self.num_lives -= 1
