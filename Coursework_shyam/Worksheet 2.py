# Write a function to find the sum and average of numbers in a list, L.
import random

L = [x for x in range(0,11) if x%2==0]

def sum(L):
    total = sum(i for i in L)
    return total

print(sum(L))

# Write a function to find the minimum and maximum number in a list, L.
# Write a program to find the even numbers in a list, L.
# Write a program to print the duplicate elements in a list, L.
# Write a program to subtract two matrices, m1 and m2, using a list of lists.
# Write a program to extract elements of a list, if it occurs more than k times.
# Write a program to remove all occurrences of an element from a list, L.
# Write a program to extract words from a string list, L whose first character is k.
# Write a program to iterate over a dictionary and print key and values
# Write a program to sum all values of a dictionary.
# Write a program to find the maximum and minimum value of a dictionary
# Write a program to implement an insertion sort algorithm
# Given a dictionary with a values list, extract the key whose value has the most unique values.
# Input : test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output : "Best"
# Explanation : 3 (max) unique elements, 9, 6, 5 of "Best".
#
# Remove all duplicate words from given sentence using a dictionary
