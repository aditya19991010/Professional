import sys
import bdbh101_report
import bdbh101_report as wr
from bdbh101_report import get_description
from bdbh101_report import get_description as do_it
from sources import daily, weekly
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import itertools



def main():
    print('Program arguments:', sys.argv)

    #  A module is just a file of Python code.
    # We refer to code of other modules by using the import statement. This makes the
    # code and variables in the imported module available to your program.
    description = bdbh101_report.get_description()
    print("Today's weather:", description)

    # Import a Module with Another Name
    description = wr.get_description()
    print("Today's weather:", description)

    # Import Only What You Want from a Module
    description = get_description()
    print("Today's weather:", description)

    description = do_it()
    print("Today's weather:", description)

    # module search path
    # It uses a list of directory names and ZIP
    # archive files stored in the standard sys module as the variable path. You can access
    # and modify this list.
    for place in sys.path:
        print(place)

    ### packages - multiple files in a folder
    # To allow Python applications to scale even
    # more, you can organize modules into file hierarchies called packages.
    print("Daily forecast:", daily.forecast())  # from sources package
    print("Weekly forecast:")
    for number, outlook in enumerate(weekly.forecast(), 1):
        print(number, outlook)

    ### Python standard library
    # One of Python’s prominent claims is that it has “batteries included”—a large standard
    # library of modules that perform many useful tasks, and are kept separate to avoid
    # bloating the core language.

    ### Handle Missing Keys with setdefault() and defaultdict()
    # setdefault
    periodic_table = {'Hydrogen': 1, 'Helium': 2}

    # trying to access a dictionary with a nonexistent key raises an exception.
    # Using the dictionary get() function to return a default value avoids an exception
    # The setdefault() function is like get(), but also assigns an item to the
    # dictionary if the key is missing
    # If the key was not already in the dictionary, the new value is used:
    # If we try to assign a different default value to an existing key, the original value is
    # returned and nothing is changed:

    carbon = periodic_table.setdefault('Carbon', 12)
    helium = periodic_table.setdefault('Helium', 947)

    ##
    # print(periodic_table['Nitrogen']) # exception
    print(periodic_table.get('Nitrogen')) # returns None if the key is not present
    print(periodic_table.setdefault('Nitrogen', 45)) # returns 45


    ### defaultdict
    # defaultdict() is similar, but specifies the default value for any new key up front,
    # when the dictionary is created. Its argument is a function. In this example, we pass
    # the function int, which will be called as int() and return the integer 0:

    # print(periodic_table['Nitrogen']) # error

    # initialize with default values
    periodic_table = defaultdict(int)
    print(periodic_table['Lithium'])  # 0 will be the output

    lead_dict = defaultdict(lambda: 'MyDefaultValue')
    lead_dict['hydrogen']=23
    print(lead_dict['helium']) # the default value MyDefaultValue will be printed


    # another example of defaultdict
    dict_counter = {}
    for food in ['spam', 'spam', 'eggs', 'spam']:
        if not food in dict_counter:
            dict_counter[food] = 0
        dict_counter[food] += 1

    for food, count in dict_counter.items():
        print(food, count)

    # using defaultdict
    food_counter = defaultdict(int)
    for food in ['spam', 'spam', 'eggs', 'spam']:
        food_counter[food] += 1


    ### Count Items with Counter()
    breakfast = ['spam', 'spam', 'eggs', 'spam']
    breakfast_counter = Counter(breakfast)
    print(breakfast_counter)
    # The most_common() function returns all elements in descending order, or just the top
    # count elements if given a count
    print(breakfast_counter.most_common())
    print(breakfast_counter.most_common(1))

    lunch = ['eggs', 'eggs', 'bacon']
    lunch_counter = Counter(lunch)
    print(breakfast_counter + lunch_counter)
    print(breakfast_counter - lunch_counter)
    print(lunch_counter - breakfast_counter)
    print(breakfast_counter & lunch_counter)
    print(breakfast_counter | lunch_counter)

    ### Order by Key with OrderedDict()
    # order of keys in a dictionary is not predictable: you might add keys a, b, and c in that
    # order, but keys() might return c, a, b.
    scores = {"Shubham": 128, "Virat": 110, "Rahul": 86, "Dhoni": 86}
    for score in scores:
        print(score)

    # An OrderedDict() remembers the order of key addition and returns them in the
    # same order from an iterator.
    scores = OrderedDict([('Shubham', 100),('Rohit', 0), ('Virat', 50)])
    for score in scores:
        print(score)

    ### Stack + Queue == deque
    # A deque (pronounced deck) is a double-ended queue, which has features of both a
    # stack and a queue. It’s useful when you want to add and delete items from either end
    # of a sequence.
    # The function popleft() removes the leftmost item from the deque and
    # returns it; pop() removes the rightmost item and returns it.
    def palindrome(word):
        from collections import deque
        dq = deque(word)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True

    print(palindrome("racecar"))
    print(palindrome("abcd"))

    # Iterate over Code Structures with itertools
    # itertools contains special-purpose iterator functions. Each returns one item at a
    # time when called within a for … in loop, and remembers its state between calls.
    # chain() runs through its arguments as though they were a single iterable:
    for item in itertools.chain([1, 2], ['a', 'b']):
        print(item)

    # # cycle() is an infinite iterator, cycling through its arguments:
    # for item in itertools.cycle([1, 2]):
    #     print(item)

    # accumulate() calculates accumulated values. By default, it calculates the sum:
    for item in itertools.accumulate([1, 2, 3, 4]):
        print(item)

    def multiply(a, b):
        return a * b

    for item in itertools.accumulate([1, 2, 3, 4], multiply):
        print(item)

    ### Print Nicely with pprint()
    from pprint import pprint
    quotes = OrderedDict([('Rohit', 'Indian cricket team captain'),('Jasprit', 'The bowler!'),('Gill', 'Opener!'),])
    print(quotes)
    pprint(quotes)



# Construct to not include whole program in other includes
if __name__ == "__main__":
    main()