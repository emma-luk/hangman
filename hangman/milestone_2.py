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
print("You entered:", guess)