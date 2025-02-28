#!/usr/bin/env python
#Open the file in reading mode
f = open("C:/Users/HomePC/Documents/Mechatronics/data.txt" , "r")
#red the whole file
print(f.read())
print(f.readline())


f = open("C:/Users/HomePC/Documents/Mechatronics/data.txt" , "a")

f.write("It is fun learning python")

print(f.readline())
f.close
#print(f.readline())