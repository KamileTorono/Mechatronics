#!usr/bin/env python

#The if statement
#Checks whether a condition is true, and if it is, IT RUNS THE BLOCK A CODE THAT FOLLOWS

"""""
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
"""""


#The else statement
#It is used to specify what happens if the condition in the if statement is false

"""
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
"""

""""
#combining f string and else stament
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f" {name}, You are an adult")
else:
    print(f" {name}, You are a minor")
"""

#The elif statement (else if)
grade = float(input("Enter your grade: "))
if grade >= 95:
    print("Yeeh, You got an A+")
elif 90 <= grade <95:
    print("You got and A")
elif 85 <= grade < 90:
    print("You have managed to get B+, poor you")
else:
    print("You have failed looser haha")