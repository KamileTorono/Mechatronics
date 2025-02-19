#!usr/bin/env python

from array import *
"""
#Arrays
ages = array('i' ,[23,45,67, 78, 29]) # i - intigers

print(ages[0])
print(ages[1])
print(ages[2])
print(ages[3])
print(ages[4])
print(ages[-1])
print(ages[-3])
print(ages[-6])

#giving the number of characters, counting how many characters are there
print(len(ages))
"""

#Assignment, to print an array of 5 numbers

numbers = array('i' , [100, 200, 300, 400, 500]) #intigers
"""
print(len(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
"""

print(numbers)
numbers.append(600)
numbers.append(700)
numbers.append(800)
print(numbers)

numbers.pop()
print(numbers)

#reversing the order of the number
numbers.reverse()
print(numbers)



