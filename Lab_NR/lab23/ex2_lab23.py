# A. Create a list of numbers from 1 to 10. Create a list squares_list using comprehension
# for the squares of the numbers (squares_list) . Create a generator expression for the
# same (squares_gen) . Print squares_list and squares_gen and observe the difference.
# Iterate over both and print the values.
# B. Repeat the above for a list/generator expression of even numbers
import random
from time import process_time

print("Generating numbers between 1-10.")
number  = [x for x in range(1,11)]
print(number)

square_list = [x**2 for x in number]
print("\nsquare list\n",square_list)


square_gen = (x**2 for x in number)
print(square_gen)
print("\nsquare list generator\n",square_gen)

print("\nnext number from square list")
print(next(square_gen))
print(next(square_gen))

even_num = [even for even in number if even % 2 ==0 ]
odd_num = [odd for odd in number if odd % 2 != 0]
even_list = [x**2 for x in number]
print("\nPrinting even num list")
print(even_list)

even_gen = (x**2 for x in number)
print("\nPrinting even number generator")
print(even_gen)

print("\nPrinting even and odd numbers")
print(even_num)
print(odd_num)



#
# print("Printing square_list")
# square_list = [i**2 for i in number]
# print(square_list)
# for x in square_list:
#     print(x)
#
# square_gen = (i**2 for i in number)
# print("\nPrinting square_gen")
# print(square_gen)
# for i in square_gen:
#     print(i)
#
#
# # get even number from number list
# even_num = [2,4,6,8]
