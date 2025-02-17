#wp to print your name weight and age using command line
#python print_detail Kamile 86 37

import sys

name = sys.argv[1]
weight = sys.argv[2]
age = sys.argv[3]

print(f"I am {name}, i weigh {weight} kgs and i am {age} years old")
