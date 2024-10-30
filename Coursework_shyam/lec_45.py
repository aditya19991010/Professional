#OOP - Object oriented programming
    #HUMANS perceive the world in the forms of objects --> Motivation for flexibility for writing codes
#method of structuring a program by bundling related properties and behaviors into individual objects
    # Define a class, which is like a blueprint for creating an object
    # Use classes to create new objects
    # Model systems with class inheritance
#Object - entity , behaviour or methods, attributes or property

#Structured programming such as C,C++
# Class - abstract entity
# Object is an instantiation of a class

import math
from time import process_time_ns


class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius **2

    def cal_perimeter(self):
        return  2*math.pi*self.radius

class shape_name(circle):
    def display_name(self):
        return print(f"Name of class used is '{circle.__name__}'")

c1 = circle(3)
c2 = circle(4)
print(c1)
print("Area--> ",c1.calculate_area())
print("Area--> ",c2.calculate_area())
print("Circumference-->", c1.cal_perimeter())
print("Circumference-->", c2.cal_perimeter())

c3 = shape_name(10)
print(c3.cal_perimeter())
print(c3.display_name())


class player():
    def display(self):
        print("This person is a player")

class cricket_player(player):
    def display(self):
        print("This person is a cricket player")

    def matches(self):
        print("The person has played in 100 matches")

p = player()
p.display()
p = cricket_player()
p.display()
