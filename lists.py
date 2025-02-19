#!usr/bin/env python
#mutable, you can change the size or content
fruits = ["Lemon", "Orange", "Apple", "Kiwi", "Peaches", "Mangoes", "Guavas"]

"""
print(fruits)
fruits[0] = "Banana"
print(fruits)

fruits[6] = "Pineapple"
print(fruits)

#for loop in all fruits

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(f"i like {fruit}")
"""

fruits.append("Water melon")
fruits.append("Lime")
fruits.append("Avocado")
print(fruits)

fruits.pop()
print(fruits)

fruits.insert(3, "Pawpaw")
print(fruits)

""""
fruits.sort()
fruits.clear()
print(fruits)
"""


fruits.extend(["Tomatoes", "Cherry", "Grapes"])
print(fruits)