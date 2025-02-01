from platform import machine
from posix import eventfd
from unicodedata import numeric


def iterator():
    days= ["Monday", "Tues", "Wed"]
    fruits=['banana', 'appple','peach']
    dessert =['tiramisu', 'ice crean', 'pie', 'pudding']
    drinks = ['coffee', 'tea', 'milk']

    for days,fruits, dessert, drinks in zip(days,fruits, dessert, drinks):
        print(days, ": drink", drinks, "-eat", fruits, '-enjoy', dessert)

def sum_list():
    odd_list = [1,3,5,7,9]
    even_num = [2,4,6,8]
    prime= [2,3,5,7,11]

    for odd_list, even_num, prime in zip(odd_list, even_num, prime):
        print("odd-", odd_list, "even-", even_num, "prime-", prime)


def machine_trans(en_list, fr_list):
    for en_list, fr_list in zip(en_list, fr_list):
        print("Eng:",en_list, ", Fre-",fr_list)
    for x in range(2,-1,-1):
        print(x, end =',')

##list comprehensions
'''A comprehension is a compact way of creation a python data structure'''
#Pythonic way
    # [ expression for item in iterable ]

def comprehensions():
    # num_list = [ number for number in range(1,6) ]
    # num_list = [ number-1 for number in range(1,6) ]
    # num_list = [ number for number in range(1,6) if number % 2 == 1 ]
    # print(num_list)
    # # In a similar way, dictionary comprehension is available for dictionaries and similar for other dataset
    #
    # #nested loop
    # rows = range(1,4)
    # cols = range(6,10)
    # cells = [(rows, cols) for row in rows for col in cols ]
    # for cell in cells:
    #     print(cell)
    # for row, col in cells:
    #     print(row,col)

    #dictionary comprehension
    #{ key_expression : value_expression for expression in iterable}
    word = 'letters'
    letter_counts = {letter : word.count(letter) for letter in word}
    print(letter_counts)
    letter_counts = {letter : word.count(letter) for letter in set(word)}
    print(letter_counts)

    #set comprehension
    #{expression  for expression in iterable}
    a_set = {number for number in range(1,10) if number %3 ==2}
    print(a_set)


def main():
    #iterator()
    #sum_list()
    # en_list = ['Monday', 'Tue', 'Wed']
    # fr_list = ['lundi', 'murdi', 'mercedi']
    # machine_trans(en_list, fr_list)
    comprehensions()
if __name__=="__main__":
    main()
