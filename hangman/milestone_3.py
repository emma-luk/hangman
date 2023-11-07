while True:
    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

    # Step 3: Check that the guess is a single alphabetical character.
    if len(guess) == 1 and guess.isalpha():
        # Step 4: If the guess passes the checks, break out of the loop.
        break
    else:
        # Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
        print("Invalid letter. Please, enter a single alphabetical character.")

# After the loop, you can continue with the rest of your code.
print("You guessed:", guess)
