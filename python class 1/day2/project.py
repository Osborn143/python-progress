import random

print("Welcome to Oje number guessing game!")
print("Please select a level: easy, medium, or hard.")

# Ask the player to select a level
while True:
    level = input("Enter level (easy, medium, hard): ")
    if level in ["easy", "medium", "hard"]:
        break
    else:
        print("Invalid level. Please enter easy, medium, or hard.")

# Set the range for the random number based on the level
if level == "easy":
    low = 1
    high = 10
    max_guesses = 3
elif level == "medium":
    low = 1
    high = 50
    max_guesses = 5
else: # level == "hard"
    low = 1
    high = 100
    max_guesses = 7

# Generate a random number within the range
number = random.randint(low, high)

print(f"I'm thinking of a number between {low} and {high}. You have {max_guesses} guesses to guess it.")

# Loop until the player runs out of guesses or guesses the correct number
for num_guesses in range(1, max_guesses+1):
    guess = int(input(f"Guess {num_guesses}: "))
    
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break

if guess != number:
    print("Sorry, you ran out of guesses. The number was", number)