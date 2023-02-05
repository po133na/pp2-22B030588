#Write the definition of a Point class. Objects from this class should have a

        #a method show to display the coordinates of the point
        #a method move to change these coordinates
        #a method dist that computes the distance between 2 points

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)