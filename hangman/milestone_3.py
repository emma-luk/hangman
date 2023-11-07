def check_guess(user_guess, secret_word):
    """
    Check if the user's guess is in the secret word.

    Args:
        user_guess (str): The user's guess.
        secret_word (str): The secret word.

    Returns:
        bool: True if the guess is in the word, False otherwise.
    """
    user_guess = user_guess.lower()
    return user_guess in secret_word

def provide_feedback(valid_guess, user_guess):
    """
    Provide feedback to the user based on the validity of the guess.

    Args:
        valid_guess (bool): True if the guess is valid, False otherwise.
        user_guess (str): The user's guess.
    """
    if valid_guess:
        print(FEEDBACK_GOOD_GUESS.format(guess=user_guess))
    else:
        print(FEEDBACK_BAD_GUESS.format(guess=user_guess))

def ask_for_input():
    """
    Continuously ask the user for a letter and validate it.

    Returns:
        str: The valid user guess.
    """
    while True:
        user_guess = input("Guess a letter: ")
        if len(user_guess) == 1 and user_guess.isalpha():
            return user_guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Secret word (you can randomly select it as you did before)
secret_word = "apple"  # Replace with your code to randomly select the secret word

FEEDBACK_GOOD_GUESS = "Good guess! {guess} is in the word."
FEEDBACK_BAD_GUESS = "Sorry, {guess} is not in the word. Try again."

user_guess = ask_for_input()
valid_guess = check_guess(user_guess, secret_word)
provide_feedback(valid_guess, user_guess)

