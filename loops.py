#!/usr/bin/env python
"""
for x in range(0,6,2):#Statement
    print("My name is Kamile") #statement
    print("I am from Tanzania")
"""
""""
for x in range(0,6,2):#Statement
    print(x) #statement
"""



#Assignment
#write a program print odd numbers from 0 to 30
#write a program print factorial of rhe number given input
# number = input("Enter the number: ")
# fact_number = number * (number -1)
#write a program to calculate the volume of the cylinder
#write a program to print the first fibonancii numbers

""""
#a program that print odd numbers from 0 to 30
for x in range(0,30):
    if x % 2 != 0: #modulus operator fo checking if the number is odd
        print(x)
"""

#write a program to print factorial of the number given input

""""
import math
# program to calculate the volume of the cylinder
def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

# Taking user input for radius and height
radius = float(input("Enter the radius of the cylinder in meters: "))
height = float(input("Enter the height of the cylinder in meters: "))

# Calculate and print the volume
volume = cylinder_volume(radius, height)
print(f"The volume of the cylinder is: {volume:.4f} cubic meters")
"""

# Function to print Fibonacci sequence
def fibonacci(n):
    # First two Fibonacci numbers
    a, b = 0, 1
    # Loop to print the first n Fibonacci numbers
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b  # Update a and b

# Taking user input
num = int(input("Enter the number of Fibonacci numbers to print: "))

# Checking if input is valid
if num <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The first {num} Fibonacci numbers are:")
    fibonacci(num)