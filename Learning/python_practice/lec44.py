#setdefault, defaultdict, Counter, OrderedDict, deque

from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from typing import OrderedDict

periodic_tab = {'Hydrogen': 1, 'Helium':2}

# periodic_tab['Nitrogen'] #Throw Keyerror
print(periodic_tab.get('Nitrogen'))
print(periodic_tab.setdefault('Hydrogen')) #return the value
print(periodic_tab.setdefault('Nitrogen',43)) #If the key is unavail then it adds an element in the dictionary.
periodic_tab = defaultdict(int) #
print(periodic_tab['Lithium'])
print(periodic_tab)
print("periodic_tab['Helium']-->",periodic_tab['Helium'])

lead_dict = defaultdict(lambda : 'MydefaultValue')
lead_dict['Hydrogen'] = '23'
print(lead_dict['Hydrogen'])

breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast) #Creates a dictionary of items and counts as value
print(breakfast_counter)

print(type(breakfast_counter))
print(breakfast_counter.most_common()) #sorted order based on counts
print(breakfast_counter.most_common(1)) #prints number of sorted items in descending order, based on counts

#Working with other list
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)

print(lunch_counter)
# & | + -

print(breakfast_counter | lunch_counter)

#Ordered Dict
#order of key in a duict

scores = OrderedDict({'Shu':221, 'Jadeja':12, 'Kohli':0})
print(scores)
# order_scores = OrderedDict()


##Stacks + queue ==deque

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) >1:
        if dq.popleft() != dq.pop():
            return False
        return True
print(palindrome("NAMAN"))

