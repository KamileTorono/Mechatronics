#!usr/bin/env python
import random

# Step 1: Simulate rolling a dice
def roll_dice():
    return random.randint(1, 6) #The function will return a value to wherever it was called.

# Step 2: Get user's guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the dice roll (enter a number between 1 and 6): "))
            if 1 <= guess <= 6:
                return guess
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Step 3: Compare the guess with the dice roll and print the result
def main():
    dice_roll = roll_dice()
    guess = get_user_guess()

    print(f"The dice rolled: {dice_roll}")

    if guess == dice_roll:
        print("Congratulations! You guessed correctly!")
    else:
        print("Sorry, your guess was wrong.")

# Run the program
if __name__ == "__main__":
    main()