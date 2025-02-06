#!usr/bin/env python

"""
< less than
> greater than
>= greater than on equal to
<= less than o equal to
== equal to
!= not equal to 
"""
"""
number = 20
guess = int(input("Enter a number between 1 to 25"))

if guess == 20 :
    print("Hooray you are correct")
"""

"""  
age = int(input("Enter your age : "))

if age < 18 :
    print("You are not allowed to drink or drive")
elif age <=50 :
    print("You can drive or drink")
else :
    print("You are too old to drink")
"""
    
#Write a program for followoing
#If you earn less that 50,000 get 10% salary increass
#if you earn btn 50,000 and 100k you get a 5% increase
#if you earn more than 100k you get 2% tax

salary = int(input("Enter your current salary"))

if salary < 50000 :
    new_salary = salary * 1.1
elif salary >= 50000 and salary <= 100000:
    new_salary = salary * 1.05
elif salary > 100000:
    new_salary = salary * 0.98
else:
    print("You are not affected")

print(new_salary)
