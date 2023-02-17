#Write a Python program to calculate the area of regular polygon.

import math

n = int(input())
s = float(input())

area = (n * s**2) / (4 * math.tan(math.pi/n))

print("area", area)