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
ties
##Lec 46

#creating class hierarchy

class Person():
    def __init__(self, name):
        self.name = name

class email_person(Person):
    def __init__(self,name,email):
        super().__init__(name) #While using methods from parent class, use super() method to call the functions from parent class
        self.email = email

sachin = email_person("Sac Tendulkar", "sachin21@gmail.com")
print(sachin)
rahane = Person("Rahane")
print(sachin.name)
print(sachin.email)


class circle:
    def __init__(self, radius):
        self.radius = radius

    @property #built-in Python decorator that turns class methods into properties.
    def diameter(self):
        return 2 * self.radius

c1 = circle(24)
print("Calculating Diameter -->",c1.diameter)

class player_hidden_name():
    def  __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Inside the getter")
        return self.__name

    # @name_setter
    # def new_name(self, new_nn):
    #     print("Inside setter")
    #     new_n = self.__name == new_nn
    #     return new_n

kohli = player_hidden_name("Virat")
print(kohli.name)

class A():
    count = 0
    def __init__(self):
        A.count +=1

    @classmethod
    def child(cls): #cls -- mandatory, python keyword
        print(cls.count)

    # @staticmethod #involke

#
# a1 = A()
# a2 = A()
# print(a1)

from datetime import date

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        return print(name,age)

    @classmethod
    def frombirthyear(cls, name, year):
        print(name, year)
        return cls(name, date.today().year - year)

    @staticmethod
    def isadult(age):
        return age >18

person1 = Person("Aditya", 24)
person1 = Person.isadult(24)
print(person1)

