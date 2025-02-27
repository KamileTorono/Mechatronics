#!/usr/bin/env python

first_name = "Emanuel"
second_name = "Mkwawa"
fav_team = "Arsenal"
weight = 82
height = 163
hoby = "reading"

def tell_name(first_name, second_name):
    print(f"My name is {first_name}  {second_name}")

def team(fav_team):
    print(f"I am {fav_team} fan")

def calc_bmi(weight,height):
    bmi = weight/(height **2)
    return bmi
bmi = calc_bmi(weight, height)
print(bmi)


