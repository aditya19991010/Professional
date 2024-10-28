# #generators
import math
import time
#
# from Coursework_shyam.lec36 import functions
#

def decorators(func):
    def wrapper():
        print("1st layer of decorator")
        func()
        print("2nd layer of decorator")
    return wrapper

# @decorators
# def hello():
#     name = input("May I know your first name? ")
#     print("Hello!", name)

# hello()
#
# ## To calculate time execution of a function

def calc_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time in : ", func.__name__, end -begin)
    return inner1

@calc_time
def fact(num):
    time.sleep(1)
    print(math.factorial(num))
fact(10)

def hello_deco(func):
    def inner1(*args, **kwargs):
        print("before execution")
        return_val = func(*args, **kwargs)
        print("after execution")
        return return_val
    return inner1


# def name_spaces():
#     #visibility and scope of functions, Global scope and local scope
#

gname= "India"

def compute_tax():
    lname = "karnatka"
    gname = "MyIndia"
    print(gname)

compute_tax()

def compute_salary():
    print(gname)
compute_salary()

#use global keyword

def compute_tax():
    global gname
    lname = "karnatka"
    gname = "MyIndia"
    print(lname, locals(), id(lname))

print("updated global variable", )
compute_tax()
