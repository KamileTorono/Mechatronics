#!/usr/bin/env python
import math
# program to calculate the volume of the cylinder


# Taking user input for radius and height
radius = float(input("Enter the radius of the cylinder in meters: "))
height = float(input("Enter the height of the cylinder in meters: "))
#calculating the volume
volume = math.pi * (radius ** 2) * height
# Calculate and print the volume

print(f"The volume of the cylinder is: {volume:.4f} cubic meters")



