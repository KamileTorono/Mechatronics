#!/usr/bin/env python

#Break : is a keyword used to break the operation of a loop
"""
number = 0
while number < 10 :
    print(number)
    if number == 4 : 
        print("Number four is reached ")
        break
    number = number + 1 
# Continue
"""



for i in range(1,100):
    if i % 2 == 0:
        continue
    print(i)