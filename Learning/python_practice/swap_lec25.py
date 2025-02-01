# def swap(a,b):
#     a = a+b
#     b=a-b
#     a=a-b
#     print(f"changed value of a is {a}, b is {b}")
#     return (a,b)

def swap(a ,b) :
    a = a*b
    b = a/b
    a = a/b
    return ('Changed value of a an b are', a , b)

# def swap(a,b):
#     l = list()
#     l.append(a)
#     l.append(b)
#     b = l.pop(1)
#     a = l.pop(2)
#     print(f"changed value of a is {a}, b is {b}")
#     return(a,b)


# def swap(a,b) :
#     c = a
#     d = b
#     b = c
#     a = d
#     print(f"changed value of a is {a}, b is {b}")
#     return(a,b)


a = 4
b = 3
print(f"Initial value of a = {a}, and b = {b}")
swapped_value = swap(a,b)
print(swapped_value)
