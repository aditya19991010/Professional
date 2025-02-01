#3 Define a function apply_operation(a,b,operation) where operation is a lambda function.
#Inside apply_operation, call the operation(a,b) and return the output. Define the lambda
#functions sum, quotient, product (from Ex 1a) and difference for the two lists list_1, list_2
#similar to ex. 1 and print the output.

import random

list_1  = [random.randint(0,100) for _ in range(1,100)]
list_2  = [random.randint(1,10) for _ in range(1,10)]


def apply_operation(a,b,operation):
    return operation(a,b)

sum = lambda x,y : x+y
quotient = lambda x,y : x//y
product = lambda x,y : x*y


print( apply_operation(4,5, sum))
print([apply_operation(x,y, product) for x,y in zip(list_1,list_2)])