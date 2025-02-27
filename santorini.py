#!/usr/bin/env python
import math
# program to calculate the volume of the cylinder


# Taking user input for radius and height
def volume_cylinder(radius, height, pi):
   volume = math.pi * (radius ** 2) * height
   return volume

radius = float(input("Enter the radius of the cylinder in meters: "))
height = float(input("Enter the height of the cylinder in meters: "))
volume = volume_cylinder(radius, height, math.pi)
#calculating the volume

# Calculate and print the volume

print(f"The volume of the cylinder is {volume: .2f} cubic meters")

import if_statements