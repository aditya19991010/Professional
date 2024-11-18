
#####
# Credit(s)
# [1] Introducing Python, Bill Lubanovic
# [2] geeksforgeeks.org
#####

# lists are mutable
def listops():
    empty_list = []
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    another_empty_list = list()

    print(list('cat'))

    # convert a tuple to list
    a_tuple = ('ready', 'fire', 'aim')
    l = list(a_tuple)
    print(l)

    # split
    birthday = '1/6/1952'
    blist = birthday.split('/')
    print(blist)

    # access by index
    players = ['Sachin', 'Dhoni', 'Virat']
    print(players[0], players[1], players[2])
    print( players[-1],  players[-2],  players[-3])

    # list of lists
    small_birds = ['hummingbird', 'finch']
    extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
    carol_birds = [3, 'French hens', 2, 'turtledoves']
    all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
    print(all_birds)
    print( all_birds[0])
    print(all_birds[1][0])

    # change an element of a list. Lists are mutable
    players[1] = "Rohit"
    print(players)

    # use slices to get elements
    # [start : end : step] extracts from the start offset to the end offset - 1, skipping by step
    print(players[0:2])
    print(players[::2])
    print(players[::-2])
    print(players[::-1]) # trick to reverse a list

    # add to end by using append
    players.append("Rahul")
    print(players)

    # combine lists by using extend or +=
    players = ['Sachin', 'Dhoni', 'Virat', 'Rahul', 'Dhoni']
    bowlers = ['Bumrah', 'Jadeja']
    all_players = players + bowlers
    print(all_players)
    players += bowlers
    print(all_players)
    players.extend(bowlers)
    print(all_players)
    players.append(bowlers)
    print(players)

    # Add an item by offset with insert
    players.insert(3, "Shubham")

    # Delete an item by offset and by value
    del players[3]
    players.remove("Rahul")

    # pop
    print(players.pop())
    print(players.pop(0))

    # find an item's offset by value with index
    players.index("Dhoni")

    # test for a value using in
    "Dhoni" in players

    # count occurrences of a value using count()
    players.count("Dhoni")

    # convert to a string with join()
    separator = '*'
    joined = separator.join(players)
    print(joined)

    # sort items in a list
    players.sort() # inplace
    sorted = sorted(players)
    players.sort(reverse=True)
    numbers = [2, 1, 4.0, 3]
    print(numbers)
    numbers.sort()
    print(numbers)

    # get length using len
    len(players)

    # assign with = , copy with copy()
    # assigning with = is a reference and not a copy
    players_ref = players
    print(players_ref)
    players[0] = "Ishan"
    print(players_ref)

    players_copy = players.copy()
    players_copy = list(players)
    players_copy = players[:]
    print(players_copy)
    players[0] = "Virat"
    print(players_copy)
    print(players[:])


def tupleops():
    # unlike lists, tuples are immutable, i.e. you cannot add, delete, or change items after the tuple is defined
    empty_tuple = ()
    print(empty_tuple)
    persons = 'Rohit','Shubham','Virat','Ishan'
    print(persons)
    persons = ('Rohit','Shubham','Virat','Ishan')
    print(persons)

    # tuple unpacking
    a, b, c, d = persons
    print(a, b, c, d)

    # exchange without temp variable
    a = 5
    b = 6
    a, b = b, a
    print(a, b)

    # convert list to tuple
    mylist = ['a', 5, 'c']
    mytuple = tuple(mylist)


def dictops():
    # uses key - value pairs. Key is usually a string, but can be any immutable object
    # keys must be unique
    # dict are also referred to as associative arrays, hashes or hashmaps
    # use curly braces
    empty_dict = {}
    scores = {"Rahul": 86, "Shubham": 128, "Virat": 110, "Dhoni": 86}
    print(scores)
    print(scores["Shubham"])

    # convert using two value sequences
    lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f']]
    print(dict(lol))

    # list of two-item tuples
    lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    print(dict(lot))

    # tuple of two-item lists
    tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
    print(dict(tol))

    # a list of two-character strings
    los = ['ab', 'cd', 'ef']
    print(dict(los))

    # a tuple of two character strings
    tos = ('ab', 'cd', 'ef')
    print(dict(tos))


    # add or change an item by [key]
    dictplayers = {
        "Rohit": 78,
        "Gill": 80,
        "Kohli": 45,
    }
    dictplayers["ishan"] = 90
    dictplayers["Gill"] = 125
    dictplayers["Gill"] = 130

    # combine dict with updates
    dictnew = {
        "bumrah": 30,
        "siraj": 20
    }
    dictplayers.update(dictnew) # value from second dict wins in case of conflict

    # delete an item key with del
    del dictplayers["siraj"]
    temp = dictplayers.copy()
    dictplayers.clear()
    dictplayers = temp.copy()

    # test for a key by using in
    "Rohit" in dictplayers

    # get an item by [key]
    dictplayers["Gill"]
    dictplayers["shyam"]
    dictplayers.get("Gill")
    dictplayers.get("Shyam", 'Not Present')

    # get all keys
    dictplayers.keys()
    print(list(dictplayers.keys()))

    # get all values
    list(dictplayers.values())

    # get all key value pairs using items
    list(dictplayers.items())


def setops():

    print('set operations')

    # sets are like a dict with its values thrown away, leaving only the keys
    # sets are unordered

    # create with a set
    empty_set = set()
    even_numbers = {0, 2, 4, 6, 8}

    # convert from other data types with set()
    new_set = set("letters")

    # set from a list
    lset = set(["Virat", "Rohit", "Shubham"])

    # set from a tuple
    tset = set(("Virat", "Rohit", "Shubham"))

    # set from a dictionary - will use only keys
    dset = set({"Virat": 80, "Rohit": 90, "Shubham": 120})

    # test for a value using in - values are set - most common usecase
    playerscores = {
        "Rohit": {53, 87, 96},
        "Virat": {123, 21, 78},
        "Shubham": {23, 44, 85}
    }
    for name, scores in playerscores.items():
        if 123 in scores:
            print(name)


    # combinations and operators
    for name, scores in playerscores.items():
        if scores & {21, 85}:  # scores intersection with 21 and scores intersection with 85
            print(name)

    a = {1, 2}
    b = {2, 3}
    print (a & b)
    print(a.intersection(b))
    print(a | b)
    print(a.union(b))
    print(a - b)
    print(a.difference(b))
    print(a ^ b)
    print(a.symmetric_difference(b))
    print(a <= b) # is a subset of b
    print(a.issubset(b))
    print(a < b) # To be a proper subset, the second set needs to have all the members of the first and more. Calculate it by using <,
    print(a >= b) # A superset is the opposite of a subset (all members of the second set are also members of the first). This uses >= or issuperset():
    print(a.issuperset(b))
    print(a > b) # And finally, you can find a proper superset (the first set has all members of the second, and more) by using >,

    # bigger data structures
    batsmen = ['Rohit', 'Virat', 'Gill']
    bowlers = ['Bumrah', 'Shami', 'Ashwin']
    keepers = ['Dhoni', 'Ishan']

    tuple_of_lists = batsmen, bowlers, keepers
    list_of_lists = [batsmen, bowlers, keepers]
    dict_of_lists = {"bat":batsmen, "bowl":bowlers, "keep":keepers}

    # tuple as a key
    houses = {(44.79, -93.14, 285): 'My House', (38.89, -77.03, 13): 'The White House'}
    print(houses[(44.79, -93.14, 285)])


# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

# Reversing a list using slicing technique
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
        return count

    # return lst.count(x)

def matrix_addition(m1, m2):
    result = []
    m1_size = len(m1)

    for i in range(m1_size):
        item1 = m1[i]
        item2 = m2[i]
        row_size = len(item1)
        row = []
        for j in range(row_size):
            s = item1[j] + item2[j]
            row.append(s)

        result.append(row)

    return result


def matrix_sum(m1, m2):
    m, item = [], []

    for item1, item2 in zip(m1, m2):
        s = len(item1)
        item = []
        for i in range(s):
            item = []
            v = item1[i] + item2[i]
            item.append(v)

        m.append(item)

    return m

def sort_dict(dict):
    sorted_dict = {}
    keys = list(dict.keys())
    keys.sort()
    for i in keys:
        sorted_dict[i] = dict[i]

    return sorted_dict


def main():
    # listops()
    # tupleops()
    # dictops()
    # setops()

    # Code examples

    # # Swap first and last element of a list
    # newList = [12, 35, 9, 56, 24]
    # print(swapList(newList))
    #
    # # Reverse a list
    # lst = [10, 11, 12, 13, 14, 15]
    # print(Reverse(lst))
    #
    # # count the number of occurrences
    # lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    # x = 10
    # print('{} has occurred {} times'.format(x, countX(lst, x)))

    # Matrix addition
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    # m = matrix_sum(m1, m2)
    m = matrix_addition(m1, m2)
    print(m)

    # Sort dictionary keys
    scores = {"Rahul": 86, "Shubham": 128, "Virat": 110, "Dhoni": 86}
    sorted_dict = sort_dict(scores)
    print(sorted_dict)




# Construct to not include whole program in other includes
if __name__ == "__main__":
    main()

# class exercise
# Write a function to find the sum and average of numbers in a list, L.
# Write a program to subtract two matrices, m1 and m2, using a list of lists.
# Write a program  to print all item values, except the last item, in a list, L
# Write a program to print the sum of alternate item values.
# Write a program to insert an item at a given position in a list  L.
# Given a list of integers, form 3 clusters, such that cluster 1 contains integers from 1 to 10,
# cluster 2 contains integers from 11 to 30 and cluster 3 contains remaining elements
# check if two strings are anagrams of each other