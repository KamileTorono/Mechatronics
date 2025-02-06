#!/usr/bin/env python
#f-string 
""""
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is {name} and i am {age} years old")
"""

""""
#iteration function
for i in range(0,5):
    print(f"My name is {name} and i am {age} years old")

#Another way
for i in range(0,5):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"My name is {name} and i am {age} years old")

#Anothet Iteration function
print( "Kamile " * 5)
"""
"""""
import math
# Loop through angles from -180 to 180 in increments of 30 degrees
for angle in range(-180, 180, 30):
   print(f"Angle {angle} : {math.cos(angle)} {math.sin(angle)} {math.tan(angle)} ")
"""
"""""
#creating Table
import math
for angle in range(-180, 180, 30):
    print(".............................................................................")
    print(f"Angle {angle} : | {math.cos(angle)} | {math.sin(angle)} | {math.tan(angle)} ")
"""

"""
#Another way
import math
print(".............................................................................")
print("|    Angle    |       cos(angle)  |     sin(angle)    |       tan(angle)  |")
for angle in range(-180, 180, 30):
    print("..............................................................................")
    print(f"Angle {angle} : | {math.cos(angle)} | {math.sin(angle)} | {math.tan(angle)} ")
"""

"""
 #ASSIGNMENT
#To plot a table of x(1-10) and the powers to 5
import math
print("..........................................................")
print("| x   | x^1  |  x^2   | x^3     |  x^4    | x^5       |   ")
print("..........................................................")
for x in range(1,11):
    print(f"| {x} :| {math.pow(x,1)}  |  {math.pow(x,2)}  |  {math.pow(x,3)}  |  {math.pow(x,4)}   |  {math.pow(x,5)} | ")
"""
    
print(".........................................")

#tabs and new lines
print("NewYork\tSeoul\tNairobi\tDaressalaam\tKampala")
print("NewYork Seoul Nairobi Daressalaam Kampala")

import math
print("...........................................")
print("x\tx^2\tx^3\tx^4\tx^5")
print("...........................................")
for x in range(1,11):
    print(f"{x}\t{math.pow(x,2)}\t{math.pow(x,3)}\t{math.pow(x,4)}\t{math.pow(x,5)} ")
print("...........................................")

print("My name is \nKamile \nTorono \nMkwawa")
