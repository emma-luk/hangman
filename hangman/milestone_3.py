# Previous code for input validation
while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Secret word (you can randomly select it as you did before)
secret_word = "apple"  # Replace with your code to randomly select the secret word

# Step 1: Create an if statement that checks if the guess is in the word.
if guess in secret_word:
    # Step 2: In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
    print(f"Good guess! {guess} is in the word.")
else:
    # Step 3: Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."
    print(f"Sorry, {guess} is not in the word. Try again.")
