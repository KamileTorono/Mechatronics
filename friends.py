#!usr/bin/env python

#use for loop to get the ages of your 5 friends
#reverse thje ages and print

from array import *

"""
ages = array('i', []) #empty array
f_ages = []
"""


#how many friends ages you want to enter?
number_ages = int(input("How many friens ages do you want to enter?"))
#create an empty list to store the names
ages = []

#use for loop to input the ages
for i in range(number_ages):
    age = input(f"Enter age {i + 1}: ")
    ages.append(age)
print(ages)
""""
#print all the ages entered
    print("Here are the ages you entered:")
    for age in ages:
         print(age)
"""