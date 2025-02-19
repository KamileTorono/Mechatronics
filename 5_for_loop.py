#!/usr/bin/env python

#loops and Iterations

#for loop
#while loop
#if statements
#if else statements
#switch case
import math

""""
#for loop
for x in range(1,6):
    print(x)

#the space is called a tab and should not be deleted

for x in range(1,21):
    print(x)
"""
""""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
"""

""""
#for loop
for x in range(1,6):
    print(x)
"""

""""
#Commulative thingy
numbers = [10,20,30,40,50]
total = 0
for number in numbers:
    total += number
    print("Total sum:",total )
"""

"""
#In order to have the total sum, the print must be OUT of the for loop
numbers = [10,20,30,40,50]
total = 0
for number in numbers:
    total += number
print(f"Total sum: {total}")

capitals = {"Tanzania":"Dodoma", "Kenya":"Nairobi", "Uganda":"Kampala"}
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
"""

#how many names you want to enter?
number_names = int(input("How many names do you want to enter?"))
#create an empty list to store the names
names = []

#use for loop to input the names
for i in range(number_names):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

#print all the names entered
    print("\nHere are the names you entered:")
    for name in names:
         print(name)