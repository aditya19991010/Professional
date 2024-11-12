# https://docs.google.com/document/d/1PdwRyJZIJiXCXZ9v2JUFMvkFhm5YO825r4QigwhnU-4/edit?tab=t.0
from tkinter import EXCEPTION

from fontTools.subset import prune_hints
from fontTools.ttLib.tables.TupleVariation import PRIVATE_POINT_NUMBERS
from numpy.testing.print_coercion_tables import print_new_cast_table
from pandas.core.arrays.timedeltas import sequence_to_td64ns
from tenacity import sleep

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [x.capitalize() for x in fruits]

# print(capitalized_fruits)

vowels=["a","e","i","o","u"]

def words_with_vowels(n,fruits):
    fruits_with_only_two_vowels = [items for items in fruits \
                                   if items.count("a") +items.count("e") \
                                   +items.count("i")+items.count("o")+items.count("u") \
                                   ==n]
    return print(fruits_with_only_two_vowels)

words_with_vowels(2,fruits)

# 3
org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]
#
# def similarity(org1,org2, threshold):
#     for seq1,seq2 in org1,org2:
#         similarity_Score = 0
#         while threshold != similarity_Score:
#             for nucl1,nucl2 in seq1,seq2:
#                 if nucl2 == nucl1:
#                     similarity_Score +=1

#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_num = {x:x**2 for x in numbers}
print("Dictionary comprehension",sq_num)

# 5.
sentence = "Hello, how are you?"
list = [x for x in sentence.split(" ")]
dict_rev = {x:x[::-1] for x in list}
print(dict_rev)


# 6.
string = "Character has different meanings"
list = [x for x in string.split(" ")]
sort_list = lambda x:x[::-1]
print(sort_list(list))

# 7.
A = [1,2,3,4,5,-7,-8,-9]
sort_neg_pos = lambda x:x.sort()
sort_neg_pos(A)
print(A)

# 8.
#create decorator
def log_decorator(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        return print(f"Calling {func.__name__} with args ({args}), and kwargs ({kwargs})")
    return wrapper

@log_decorator
def add(a,b):
    return a+b

add(2,3)

#9.
import time

def execution_time(func):
    def wrapper(*args,**kwargs):
        print(f"Starting time for execution of {func.__name__}: {int(time.time())}")
        func(*args,**kwargs)
        print(f"Ending time for execution of {func.__name__}: {int(time.time())}")
        # return func
    return wrapper

@execution_time
def check_deco_func():
    return time.sleep(2)

# check_deco_func()

# 10
def division(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError as ZDE:
        print(f"Bad response :{ZDE}")
    except ValueError as VE:
        print(f"Bad response : {VE}")
    except TypeError as TE:
        print(f"Bad response : {TE}")
    finally:
        print("Please try again.")

division(4,"a")

class FormulaError(Exception):
    def __init__(self):
        return print(f"Bad response: {FormulaError.__name__}")
    pass

def calculator():
    try:
        iteration =True
        while iteration:
            equation = str(input("Enter an equation to add/substract: ")).split(" ")
            # print(equation)
            # a = float(equation[0])
            # b = float(equation[2])
            # # c = equation[1]

            if len(equation) < 3:
                raise FormulaError
            elif equation[1] == "+" and equation[1] != "-":
                a = float(equation[0])
                b = float(equation[2])
                c = equation[1]
                print(a + b)
            elif equation[1] == "-" and equation[1] != "+":
                a = float(equation[0])
                b = float(equation[2])
                c = equation[1]
                print(a - b)
            elif equation[1] != "+" and equation[1] != "-":
                raise FormulaError
            else:
                raise IndexError
            userinput = input("Give new input or type quit: ")
            if userinput != "quit":
                break
            else:


    except ValueError as VE:
        print(f"Bad response : {VE}")
    except FormulaError as FE:
        print(f"{FE}")
    except IndexError as IE:
        print(f"Bad response : {IE}")


def main():
    return calculator()

if __name__=="__main__":
    main()