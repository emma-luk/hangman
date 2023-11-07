import random

FAVORITE_FRUITS = ["apple", "banana", "strawberry", "mango", "watermelon"]
VALID_INPUT_LENGTH = 1

def is_valid_input(input_str):
    return len(input_str) == VALID_INPUT_LENGTH and input_str.isalpha()

def main():
    randomly_selected_word = random.choice(FAVORITE_FRUITS)
    user_guess = input("Enter a single letter: ")

    if is_valid_input(user_guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()
