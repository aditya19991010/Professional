# A. Write a function ListBooksByAuthor(author) that prints the books for an author from a
# dictionary. Eg: dic1={"Jane Austen":["Pride and Prejudice","Sense and
# Sensibility"],"Charles Dickens":["Oliver Twist","Pickwick Papers"]}
# Write a decorator addPreface(func) that prints a line “These are authors of Classical
# English Literature” before invoking the function ListBooksByAuthor . After invoking the
# function, it should print (“They are to be enjoyed”. Get a list of books from the user and
# call ListBooksByAUthor. If multiple authors are entered, they are to be separated by a
# comma.


dic1={"Jane Austen":["Pride and Prejudice","Sense and Sensibility"],"Charles Dickens":["Oliver Twist","Pickwick Papers"]}

#Decorator
def addPreface(func):
    def wrapper(*args,**kwargs):
        print("These are authors of Classical English Literature")
        func_value = func(*args,**kwargs)
        print("They are to be enjoyed")
        return func_value
    return wrapper

@addPreface
def ListBooksByAuthor(*args) :
    authors = [ i for i in args ]
    literature = []
    for author in authors:
        res = literature.append(dic1[author])
    return print(literature)

ListBooksByAuthor("Charles Dickens", "Jane Austen" )


# B. Write a function addTwoNumbers(a,b) that returns the sum of a and b. Write a
# decorator @log_execute that is called as decorator from addTwoNumbers . This should
# print “Entering function addTwoNumbers at time “ and “Exiting function addTwoNumbers
# at time” before and after the call.

import time

def log_execute(func):
    def wrapper(*args):
        print(f"\nEntering function {func.__name__} at {time.time()}")
        res = func(*args)
        print(f"Exiting function {func.__name__} at {time.time()}")
        return res
    return wrapper

@log_execute
def addTwoNumbers(a,b):
    sum = a+b
    return print(f'the sum of two numbers {a} and {b} is {sum}')
addTwoNumbers(77,66)

