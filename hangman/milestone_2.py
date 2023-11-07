# Import the random module.
import random

# Step 1: Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["apple", "banana", "strawberry", "mango", "watermelon"]

# Step 2: Assign this list to a variable called word_list.
word_list = favorite_fruits

# Step 3: Print out the newly created list to the standard output (screen).
print(word_list)

# Task 2 Choose a random word from the list
# Step 3:
# Create the random.choice method and pass the word_list variable into the choice method.

# Step 4:
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Step 5: Print out the randomly selected word.
print("Randomly Selected Word:", word)

# Step 1: Using the input function, ask the user to enter a single letter.
guess = input("Enter a single letter: ")

# Step 2: Assign the input to a variable called guess.
#bbprint("You entered:", guess)

# Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
    print("Oops! That is not a valid input.")