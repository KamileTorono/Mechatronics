#!/usr/bin/env python

# ask the user for the first number 
first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number :"))

sum_number = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {sum_number}")

# data types


# string : alphabet letters / numbers / special symbols in the keyboard :a,b....z ,ABCD.....Z ,01234...9 
# % * @ !&*  " " 

grade = 'A'
# strings 
my_name = "Kamile"
#integers : positive / negative whole numbers

my_age = 37
temp = -13  

#float : positive / negative fractions / decimal point numbers  : 0.5
my_weight = 83.5
#boolean
# T / F two outputs : True / False
is_professor = False

is_married = True

print(type(grade))
print(type(my_weight))
print(type(my_age))
print(type(is_married))

#format output
print(f"My name is {my_name} and I am {my_age} years old ")
