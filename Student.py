#!/usr/bin/env python

# creating a class 

class Student:

    hobby = "swimming" #attribute
    origin = "Tanzania"

#behaviour of the Student
    def __init__(self, name, id, age, grade):
        self.name    =  name
        self.id      =  id
        self.age     =  age
        self. grade  = grade

    def print_name(self, name):
        print(f"My name is {name}")

    def print_id(self, id):
        print(f"My Id is {id}")

    def print_age(self, age):
        print(f"I am {age} years old")

    def print_grade(self, grade):
        print(f"My grade is {grade}") 


#instance of a student
student1 = Student("Kamile Torono", 1210, 37, "A") 
student2 = Student("Moses Opuru", 1205, 29, "A+")
student3 = Student("Kassim Majaliwa", 4648, 56, "B")       
        
print(student1.age)
print(student2.grade)
print(student3.name)

student3.print_age(27)
student2.print_id(1205)


class Teacher:

    def __init__(self,name, salary, subject):
        self.name = name
        self.salary = salary
        self.subject = subject


    def increase_salary(self, salary):
        new_salary = salary + (0.2 *salary)
        return new_salary
    def print_salary(self,salary):
        print(f"The Teacher earns : {salary} Tsh ")

teacher1 = Teacher("Emanuel Mkwawa", 15978903, "Biology")
teacher2 = Teacher("Jada El kasri", 55898, "Physics")


print(teacher2.salary)
new_sal = teacher2.increase_salary(70000)
print(new_sal)


