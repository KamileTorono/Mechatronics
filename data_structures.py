#!/usr/bin/env python


#turple
friends = ("Jada", "Lesley", "Mosses","Emanuel")
numbers = tuple( range(10)) 

"""
print(friends)
print(len(friends))
print(friends[0])
print(friends[1])
print(friends[2])
print(numbers)

for friend in friends:
    print(friend)

friends_lists = list(friends)
print(type(friends_lists))
friends_lists.append("Bob")
print(friends_lists)
"""





#sets
cities = {"Seoul", "Nairobi", "Dodoma", "Rabat"}

for city in cities:
    print(city)

stuff = {"Bob", 24, 45.8, True}
print(stuff)


#remove
stuff.remove("Bob")
print(stuff)


my_stuff = stuff.copy()

set_numbers  = {1,2,3,4}

print(set_numbers)
set_numbers.add(5)
set_numbers.update({6,7,8})
print(set_numbers)





#dictionaries
#special type of set taht stores data in Key:value pair

car = {"brand" : "toyota", "model": "land cruiser", "year": 2024, "fuel_cc": 2900}
print(car["brand"]) #prints the value

#use foor loop to print all the keys in dicti

for key in car:
    print(key)

for val in car.values():
    print(val)

del(car["brand"])
new_car = car.copy
print(car)
print(new_car)