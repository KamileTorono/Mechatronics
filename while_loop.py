#!/usr/bin/env python

"""
count = 10 # initial condition
while count > 0 :
    count = count - 1
    print(count)
"""


"""
counter = 1
while counter <=5:
    print(counter)
    counter += 1
"""

"""
# Example: Keep asking for input until the user enters 'yes'
response = ""
while response != "yes":
    response = input("Do you want to exit? (Type 'yes' to exit): ")

print("Exiting the loop.")
"""



#while loop with break


"""
num = 1
while True:
    print(num)
    num += 1
    if num > 5:
        break
print("this is the limit bozo")


#loop with continue
#The continue statement is used to skip the current iteration and immediately jump to the next iteration of the loop. In other words, when continue is encountered, the rest of the code inside the loop after continue is ignored for that iteration, but the loop continues with the next iteration.
#Example: skip printing number 3 using continue

num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

#While loop with else clause
#Else part executes if the loop completes without a break

num = 1
while num <=3:
    print(num)
    num += 1
else:
    print("Loop ended successfully")

#Skip invalid input

num = 10
while num < 30:
    num += 1
    if num % 2 == 0:
        continue #Skip even numbers
    print(num)

"""

#using break to exit a search early
target = 70
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0

while i < len(numbers):
    if numbers[i] == target:
        print(f"Found {target} at index {i}")
        break #stop searching once target is found
    i += 1


#Using continue to filter data

data = [15, 0, -4, 20, 30, -10]
i = 0
while i < len(data):
    if data[i] < 0:
        i += 1
        continue #skip negative values
    print(f"Processing data : {data[i]}")
    i += 1