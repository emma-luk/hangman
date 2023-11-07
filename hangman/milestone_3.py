def check_guess(guess, word):
    # Step 2: Convert the guess into lowercase.
    guess = guess.lower()

    # Step 3: Check if the guess is in the word.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    while True:
        # Step 2: Move the code for input validation into this function.
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word.
            check_guess(guess, word)
            return  # Exit the loop when valid input is provided
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Secret word (you can randomly select it as you did before)
secret_word = "apple"  # Replace with your code to randomly select the secret word

# Step 4: Call the ask_for_input function to test your code.
ask_for_input(secret_word)
