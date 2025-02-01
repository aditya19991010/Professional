import random

#1
list_1  = [random.randint(0,100) for _ in range(1,100)]
list_2  = [random.randint(1,10) for _ in range(1,10)]

even= lambda x:True if x%2==0 else False
odd = lambda x:True if x%2!=0 else False

filter_even = list(filter(even,list_1))
filter_odd = list(filter(odd, list_2))

cube  = lambda x: x**3
square  = lambda x : x**2
product  = lambda x,y : x*y
square_cube = lambda x:square(cube(x))

print("Filter even numbers",filter_even)
print("Filter odd numbers",filter_odd)
print("Cubes -->",[cube(i) for i in list_1])
print("Squares -->", [square(x) for x in list_1])
print("Squares Cubes -->",[square_cube(x) for x in list_1])
print("Product of lists -->",[product(x,y) for x,y in zip(list_1, list_2)])
