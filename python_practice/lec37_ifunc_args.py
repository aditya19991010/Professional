# from traceback import print_tb
#
# fruits = ['mango', 'kiwi','apple', 'pineapple']
#
# cap_fruits = {fruits[x].capitalize() for x in range(len(fruits)) }
# print(cap_fruits)
#
# vowel = ('a','e','i','o','u','e')

''' Build a function that can take the variable number of arguments, use *args in the functions'''
from posix import putenv
from readline import set_completion_display_matches_hook


def print_args(*args):
    for i in args:
        x = print(str(args))
        return  x
    # print("Positional argument tuple : ", args) #Another method

print_args("Rohit", "Kohli", "Mogli", "Aditya")

def print_more(required1, required2, *args):
    print('Need this one : ', required1)
    print('Second positional arg : ', required2)
    print('Remaining args : ', args)

print_more("Laali", "Kaali", "Muchhad", "Pagal")

def print_kwargs(**kwargs):
    print('Keyword argument', kwargs)
    print(kwargs.keys())
    print(kwargs.values())

print_kwargs(name="Sita", twin_name="geeta")

def run_something_with_other_func(func, args1, args2):
    print("Calling func within func")
    func(args1, args2)

run_something_with_other_func(print_args, "Rohit", "Kohli")


##Inner functions

def outer(a,b):
    def inner(c,d):
        sum = c+d
        return sum
    return a+b
    print("Completed another outer and inner function")

print(outer(100,122))


def knights2(saying):
    def inner2():
        return  "We are the knights who are saying : '%s'" % saying
    return inner2


a = knights2("Duck")
print(type(a))
b = knights2("Haseofeffer")
print(a())

##Lambda functions

num = [1,2,3,4,5]
square_num(num, square_func)

square_num(num, lambda n: n*n)