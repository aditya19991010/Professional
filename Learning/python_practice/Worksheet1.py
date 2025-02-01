'''Write a function to find the sum of squares of first N numbers
Write a function to convert the decimal number D into binary.
Write a function that computes the number of 1s in a binary representation of a decimal number, N.
Write a function to convert the binary number B into decimal.
Write a function that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.
Write a function to check if a given number, N, is prime or not
Write a function to print individual digits of a number, N.
Write a function to print the first half of a string, S.
Write print alternate characters of a string, S
Write a program to concatenate two strings, S1 and S2.
Write a function to find the first occurrence of a character, c, in a string S.
Write a function to find the  highest frequency character in a string, S.
Write a function to replace all occurrences of a character, c,  with another character, d.
Write a function to trim leading whitespace characters from a string, S.
Write a function to count the number of occurrences of a word, W, in a sentence, S.
Write a function to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams
'''
from pydoc import replace
from stat import S_IREAD
from tkinter.ttk import Treeview

from numpy.ma.core import count

from PycharmProjects.Work.Coursework_shyam.lec35 import machine_trans


#Write a function to find the sum of squares of first N numbers

# def sum_square(num):
#     z = int()
#     while num != 0 :
#         y = num**2
#         num = num - 1
#         z = z + y
#     return z
#
#
# def main():
#     num = 5
#     x = sum_square(num)
#     print(x)
#
# if __name__=="__main__":
#     main()


#Write a function to convert the decimal number D into binary
# Conversion steps:
#
#     Divide the number by 2.
#     Get the integer quotient for the next iteration.
#     Get the remainder for the binary digit.
#     Repeat the steps until the quotient is equal to 0.
# def cnvrt_dec_binary():
#     while num % 2 != 0:
#         y = num % 2
#

# Write a function that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.
def power_calc(base, power):
    result = base**power
    return result

# Write a function to check if a given number, N, is prime or not
def check_prime(n):
    while n != 0:
        n = n-1
        if n/ n-1 ==0:
            print("This is a prime number")
        else:
            print("This is not a prime number")

#Write a function to print individual digits of a number, N.
def write_digits(num):
    num =list(str(num))
    for i in range(len(num)):
        prompt=print(num[i], end='')
    return prompt

#Write a function to print individual digits of a number, N.
def print_digits(num):
    num  = str(num)
    num_list = []
    for i in range(len(num)):
        num_list.append(num[i])
    return print(num_list)

def print_digits2(num):
    num = str(num)
    num_list = []
    [num_list.append(num[x]) for x in range(len(num))]
    return print(num_list)

#Write a function to print the first half of a string, S.
def half_string(string1):
    length = len(str(string1))
    half_len = length/2
    return print(string1[:int(half_len)])

half_string("ADITYANAMAN")


#Write print alternate characters of a string, S
def alt_charac(string1):
    return print(string1[::2])
alt_charac("asdfghjk")

# Write a program to concatenate two strings, S1 and S2.
def conc_str(string1, string2):
    concat= string1 + string2
    return print(concat)

conc_str("Aditya", "NAMAN")

# Write a function to find the first occurrence of a character, c, in a string S.
def find_c(string1):
    string1_list = list(string1)
    if "c" in string1_list :
        print(f"Letter 'c' found in string {string1}")
    else:
        print(f"'c' is absent in the string {string1}")

# find_c("hasfb")


# Write a function to find the  highest frequency character in a string, S.
def highest_freq(string1):
    set_s = tuple(S)
    dict_1 = {}
    S_counts = []
    for i in range(len(S)):
        dict_1[set_s[i]] = S.count(set_s[i])

    keys_list = list(dict_1.keys())
    val_list = list(dict_1.values())

    max_occurence = max(dict_1.values())
    key_max_freq = keys_list[val_list.index(max_occurence)]
    print(f"'{key_max_freq}' has the highest frequency")

S = "aaaaaabdvbfyhbs"
highest_freq(S)


# def letter_freq(S):
#     s_set = set(S)
#     s_list = list(S)
#     count_dict = {s_set}
#
#     for letters in range(len(s_set)):
#         print(s_list.count(s_set[letters]))

# letter_freq("asfadfadf")

string4 = "adfasgkjbsgd"

print(list(string4).count("a"))

# Write a function to replace all occurrences of a character, c,  with another character, d.
##basic way

string1 = "cocoon"
pattern = "c"
replace_by = "d"

def replace_c_to_d(string1, pattern, replace_by):
    print(f"Before replacing  {pattern} with {replace_by}", string1)
    string1 = string1.replace(pattern, replace_by)
    return print(f"After replacing {pattern} with {replace_by}", string1)

replace_c_to_d(string1, pattern, replace_by)

##complex way
# def replace_c_to_d(string1, pattern, replace_by):
#     string1 = list(string1)
#     for i in range(len(string1)):
#         if string1[i] == "c" :
#             string1.remove("c")
#             string1.insert(i, "d")
#     string1 = str(string1)
#     return print(f"After replacing {pattern} with {replace_by}" , string1)
###requires removal of ',' and '[]'

# Write a function to trim leading whitespace characters from a string, S.
string1 = "Hey!, We are planning for a great grand celebration."
def remove_whitespaces(string1):
    string1=string1.replace(" ", "")
    return print(f"After removing whitespaces with in the sentences : ", string1)

remove_whitespaces(string1)

# Write a function to count the number of occurrences of a word, W, in a sentence, S.

alphabet = "w"
string1 = "What a great celebration you have done, We are witnessing the world greatest show."

def count_occurence(string1, alphabet):
    string1 = string1.lower()
    counts = string1.count(alphabet)
    return print(f"Total counts of {alphabet} is {counts}")

count_occurence(string1, alphabet)

# Write a function to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams
word = "Worth"
anagram = "Throw"

word = tuple(word.lower())
anagram = tuple(anagram.lower())

# generate all the possible words
while word != tuple(anagram.lower()):
    print(f"This is an anagram")


def check_anagram(word, anagram):
    word = tuple(word.lower())
    anagram = tuple(anagram.lower())
    # generate all the possible words
    while word != tuple(anagram.lower()) :
        print(f"This is an anagram")


