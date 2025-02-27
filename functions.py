#!/usr/bin/env python

#function - block of code or statements excecuted together
#function definition


""""
name = "Kamile"
country = "Tanzania"
age = 37






def print_details():
    #body of the function
    print(f"My name is {name}") # line of code or statement
    print(f"I am {age} years old") # line of code or statement
    print(f"I a m from {country}") # line of code or statement

print_details()


def print_details(name,age,country):
    #body of the function
    print(f"My name is {name}") # line of code or statement
    print(f"I am {age} years old") # line of code or statement
    print(f"I a m from {country}") # line of code or statement

print_details("Emanuel", 35, "Tanganyika")


def add_numbers(x,y):
    return x + y 
sum_numbers = add_numbers(10,30)
print(sum_numbers)

def multiply_numbers(x,y):
    return x * y
product_numbers = multiply_numbers(50,12)
print(multiply_numbers)
"""
import math
#calculate volume of cylinder and area of cycle

def volume_cylinder(radius, height, pi):
    volume = pi * radius * radius *  height
    return volume
volume = volume_cylinder(5,3,math.pi)
print(volume)


#Area of circle

def area_circle(pi, radius):
    area = math.pi * (radius **2)
    return area
radius = float(input("Enter the radius of cirlce in m: "))
area = area_circle(math.pi, radius)

print(f"The Area of the circle is {area: .2f} m2 ")

