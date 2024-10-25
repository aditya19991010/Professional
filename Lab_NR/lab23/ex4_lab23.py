#A. Create a Function called CreateRepeats(n) that has an inner function repeat(string).
# This should repeat the string n times. The outer function CreateRepeats should return
# the inner function repeat . Create another function repeat_10 that calls
# CreateRepeats(10) and obtain repeat_10 as output function. Call repeat_10 with the
# string “Hello” as input . Observe the output.
from logging.config import RESET_ERROR
from typing import Concatenate
from venv import create


def CreateRepeats(n):
    def repeat(string):
        res = string*n
        print(res)
    repeat(string)

string = "Hello"
n = 5
# repeat_10_times = CreateRepeats(10)
# repeat_10_times("Hi")

def repeat_10(string = "Hello"):
    def CreateRepeats(n=10):
        res = string*n
        print(res)
    CreateRepeats()

CreateRepeats(n)
repeat_10(string)




# Repeat the above with CreateExponent(n) with the inner function exponent(m) that
# should return m**n. Create functions get_square, getCube by calling CreateExponent
# with 2, 3 as arguments. Call get_square, get_cube with different numbers and check the
# output.

def CreateExponent(n):
    def exponent(m):
        res = m**n
        return res
    return exponent

get_square = CreateExponent(2)
get_cube = CreateExponent(3)
print("Square of 3: ", get_square(3))
print("Cube  of 3: ", get_cube(3))



