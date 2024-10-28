# A. Write a function that prints a global counter initialized to 1. The local variable counter
# (initialized to 10) should be printed every time it is called as well. Use decorators to
# increment the global counter before the function is called.


i = 1 #global counter
print(globals())

#decor
# def increment(func):
#     i +=1
#     func()
#     return increment
#
# @increment
def local_var():
    i =1
    local_var()

    return print(i)

local_var()



# B. Define a global variable named shared_value and set it to 5. Write two functions:
# add_to_shared_value(n): Adds n to shared_value using the global keyword.
# multiply_shared_value(n): Multiplies shared_value by n using the global keyword. Call
# these functions in different orders and print shared_value after each call to observe how
# it changes using decorators (log_decorator)