#!/usr/bin/env python

# CREATE A CLASS NAMED My_class

class My_class:
    x = 5  # x is a property of My_class

    # Create an object named p1 and print the value of x
"""
p1 = My_class()
print(p1.x)



class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
person1= Person("Kam",35)
person2 = Person("Jada", 23)

print(person1.name)
print(person1.age)
print(person1)
print(person2)

print(person2.name)
print(person2.age)


class My_cars:
    def __init__(self,name, model, transmission):
        self.name= name
        self.model = model
        self. transmission = transmission
car1 = My_cars("Toyota", "Land Cruiser", "Manual")
print(car1.name)
print(car1.model)
print(car1.transmission)

car2 = My_cars("Toyota", "RAV 4", "Automatic")
print(car2.name)
print(car2.model)
print(car2.transmission)

car3 = My_cars("Toyota", "Harrier", "Manual")
print(car3.name)
print(car3.model)
print(car3.transmission)
"""

"""
#with __str__()  function
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

       
   def __str__(self):
        return f"{self.name}({self.age})" # we could make this more presentable the way we feel return f"Hello My name is {self.name} and I am {self.age} years old"


person1= Person("Kam",35)
person2 = Person("Jada", 23)
print(person1)
print(person2)
"""


"""
#Object Method
#Insert a function that prints a greeting, and execute it on the person1 object:

class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

       
   def __str__(self):
        return f"{self.name}({self.age})" # we could make this more presentable the way we feel return f"Hello My name is {self.name} and I am {self.age} years old"

   def greet(self):
       print(f"Heloo My name is {self.name} and I am {self.age} years Old " ) 

person1= Person("Kam",35)

person2 = Person("Jada", 23)

print(person1)
person1.greet()

print(person2)
person2.greet()
"""


"""
#Modification
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

       
   def __str__(self):
        return f"{self.name}({self.age})" # we could make this more presentable the way we feel return f"Hello My name is {self.name} and I am {self.age} years old"
person1= Person("Kam",35)

person2 = Person("Jada", 23)
print(person1)
print(person1.name)
print(person1.age)
print(person2)
print(person2.name)
print(person2.age)


#CHANGE NAME AND AGE
person1.age = 30 #modifying age
person2.age = 70
person1.name = "Emanuel" #modifying name
person2.name = "Jade"

print(person1)
print(person1.name)
print(person1.age)
print(person2)
print(person2.name)
print(person2.age)
"""

"""
#DELETING PROPERTIES ON OBJECT

class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

       
   def __str__(self):
        return f"{self.name}({self.age})" # we could make this more presentable the way we feel return f"Hello My name is {self.name} and I am {self.age} years old"
person1= Person("Kam",35)

person2 = Person("Jada", 23)

print(person1)
print(person1.name)
print(person1.age)
print(person2)
print(person2.name)
print(person2.age)

del person1.age
del person2.name

print(person1)
print(person1.name)
print(person1.age)
print(person2)
print(person2.name)
print(person2.age)
"""

class Person:
    pass