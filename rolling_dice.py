#!usr/bin/env python
import random

def rolling_dice(): #def keyword is used to define function which is rolling_dice
    # Simulate rolling a dice by generating a random number between 1 and 6
    return random.randint(1, 6) #The function will return a value to wherever it was called and generates a random integer between 1 and 6, simulating the roll of a six-sided dice.

def guess_dice():
    # Guess the number of the dice that will be rolled
    guess = int(input("Guess the dice roll from  (1-6): "))
    return guess #The function will return a value of a guessed number 

def play_dice_game():
    rolled_value = rolling_dice()
    guessed_value = guess_dice()

    print(f"The dice rolled is number: {rolled_value}")
    
    if guessed_value == rolled_value:
        print("Congratulations! You guessed it right.")
    else:
        print("Sorry, wrong guess. Better luck next time!")

# Start the dice game
while True:
    play_dice_game()
