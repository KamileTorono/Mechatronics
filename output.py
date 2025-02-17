#!/usr/bin/env python
#how to formart the characters

#String - collection of characters
 
name = input("Enter your name: ")
city = input("Where are you from?: ")
print( "My name is {0} and i am from {1}.".format(name ,city))

#CameLcase
fav_team = "Arsenal"
first_name = "Emanuel"
secondName = "Mkwawa"
cityOfOrigin = "Arusha"
weight = 82.4

print(" I am %s and I weigh %f " %(first_name ,weight))
print(" My father is %s and I am from %s " %(secondName,cityOfOrigin))

#f String
print(f"My name is {first_name} and I am from {city} and i weight {weight}" )

#Challenge printing Age, fav food and hobie in one line
age=37
fav_food = "Ugali"
hobie = "Movies"

print(f"I am {age} years old and i like to eat {fav_food} and watching {hobie} ")

#another f-string method
f_string = f" I am from {city} and i like watching {hobie}"
print(f_string)

pi=3.141592654
print(f"The value of pi is {pi}")
print("The value o fpi is %.3f" %(pi))
print("The value o fpi is %.2f" %(pi))

#food = "chapati"
#calories = 70
