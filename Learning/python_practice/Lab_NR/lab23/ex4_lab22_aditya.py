#4 Create a function create_exponent that takes n as a parameter and returns a lambda
# function that is x raised to the power n.

import random

list_1  = [random.randint(0,100) for _ in range(1,100)]
list_2  = [random.randint(1,10) for _ in range(1,10)]


def create_exponent(n):
    return lambda x: x**n

create_4th_exponent = create_exponent(4)
create_5th_exponent= create_exponent(5)

print([create_4th_exponent(x) for x in list_2])
print([create_5th_exponent(x) for x in list_2])