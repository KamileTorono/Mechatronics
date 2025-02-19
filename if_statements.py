#!/usr/bin/env python

#Program that calculate the tax of civil servants

# 0-50000 ... 6% tax 
#50001 ----- 100000   15% tax
#100000 ------ 500000 20% taz
# above 500000   25%

#get user salary
""""
salary = float(input("Enter your current salary : "))

new_salary = 0.0

if salary < 50000 :
    tax = (6 * salary /100)
    new_salary = salary - tax
 
elif salary > 50000 and salary < 100000:
    tax = (15 * salary /100)
    new_salary = salary - tax
 
elif salary > 100000 and salary < 500000:
    tax = (20 * salary /100)
    new_salary = salary - tax

else:
    tax = (25 * salary/100)
    new_salary = salary - tax

print(f"Your Salary after tax is {new_salary}")
"""

education = int(input("Enter your years of study: "))
if education >= 10:
    print("Your salary is 500k USD")
elif 6 <= education <= 9:
    print("Your salary is 300k USD")
elif 5 <= education <= 3:
    print("Your salary is 200k USD")
else:
    print("Work hard your salary is below 100k USD")