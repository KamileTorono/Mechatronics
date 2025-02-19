#!usr/bin/env python
#randomm module - a module used in guesing random numbers

import random

def roll_dice(): #def keyword is used to define function
    # Simulate rolling a dice by generating a random number between 1 and 6
    return random.randint(1, 6) #


def play_dice_game():
    rolled_value = roll_dice()
  
    print(f"The dice rolled: {rolled_value}")
    
    

# Start the dice game
play_dice_game()
