# Welcome to BDBH101 - Python Programming

import time
import math
import numpy as np
import pandas as pd

def HelloWorld():
      print('Hello World !')
      print("Hello World !")
      print("It's raining in Bangalore")
      print('''Will it rain tomorrow ?''')

      # comments
      # Meaningful text is specified as comments for code readability. This is an example of single line comment
      '''
      Line 1
      Line 2
      '''

def Convert_Farenheit_Celcius(f):
      # Mathematical formula to compute celcius value from farenheit value
      c = (5/9) * (f - 32)

      return (c)

def Swap(a, b):
      temp = b
      b = a
      a = temp

      return (a, b)

def Check_Odd_Even(n):
      if (n % 2 == 0):
            out = "Even"
      else:
            out = "Odd"

      return (out)

def SumOfN(n):
    start = time.time()

    theSum, count = 0, 0

    while(count <= n):
        theSum = theSum + count
        count = count + 1

    end = time.time()
    total_time = end - start

    return (theSum, total_time)

def fib(n):
    a = 0
    b = 1

    for i in range(0, n):
        next_num = a + b
        print(next_num)

        a = b
        b = next_num

def palindrome(s):

    palin = True

    '''
    length = len(s)
    half = math.floor(length/2)
    lastpos = length-1
    for i in range(0, half):
        if (s[i] != s[lastpos]):
            palin = False
            break
        lastpos -= 1
        
    '''

    if (s == s[::-1]):
        palin = True
    else:
        palin = False

    return(palin)

def stringops(s):
    print("The original string is %s" % s)
    print(s[0], s[1])

    # strings are immutable
    # s[0] = 'a'

    # string concatenation
    new_word = s + ' located in Bangalore'
    print(new_word)

    # slicing with [start:end:step]
    print(s[:]) # entire sequence
    print(s[1:]) # starting from position 1 till the end
    print(s[:5]) # from the beginning to the end offset -1
    print(s[0:4]) # from start offset (0)the end offset (5) - 1
    print(s[0:9:2]) # start offset to the end offset -1, skipping characters by 2
    print(s[::-1]) # prints in revere order

    string_length = len(s)
    print(string_length)

    # split based on delimiter
    tokens = s.split(' ')
    print(tokens)

    # join the split tokens
    s1 = ' '.join(tokens)
    print(s1)

    # check if a string starts with some othe string
    s2 = s.startswith("Welcome")
    print(s2)

    # check if a string ends with another specified string
    s3 = s.endswith("IBAB")
    print(s3)

    # first occurrence of a word
    word = "IBAB"
    s4 = s.find(word)
    print(s4)

    # last occrrence of a word
    word = "to"
    s5 = s.rfind(word)
    print(s5)

    # count
    word = 'to'
    s6 = s.count(word)
    print(s6)


def kmers(s, k):
    str_length = len(s)
    for i in range(0, str_length-k+1):
        kmer = s[i:i+k]
        print(kmer)


# Main function
def main():
    # Let's begin

    '''
    HelloWorld()
    '''


    '''
    # Convert Farenheit to Celcius
    f = 100.0
    c = Convert_Farenheit_Celcius(f)
    print("Farenheit = %0.2f, Celcius = %0.2f" % (f, c))
    '''


    # exercise - convert Celcius to Farenheit
    # f = (9/5)*C + 32


    '''
    # Swap two numbers
    a = 5
    b = 7
    print("a = %d, b = %d" % (a, b))
    new_a, new_b = Swap(a, b)
    print("New a = %d, New b = %d" % (new_a, new_b))
    '''

    '''
    # Check if a given number is odd or even
    n = 30
    out = Check_Odd_Even(n)
    print("Number %d is %s" % (n, out))
    '''

    '''
    # sum of first N numbers
    n = 5
    s, time = SumOfN(n)
    print("Sum of first %d numbers is %d " % (n,s))
    '''

    '''
    # First 10 fibonacci numbers
    fib(10)
    '''

    # class exercises
    #   - sum of squares of first N numbers
    #   - convert the decimal number D into binary.
    #   - write a function that computes the number of 1s in a binary representation of a decimal number, N.
    #   - Convert the binary number B into decimal.
    #   - Write a function that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.
    #   - write a function to check if a given number, N, is prime or not
    #   - print individual digits of a number, N.



    '''
    # demonstrate various string operations
    s = 'Welcome to IBAB'
    stringops(s)
    '''

    '''
    s = "racecar" #"malayalam"
    p = palindrome(s)
    if (p):
        print("The word %s is a palindrome" % s)
    else:
        print("The word %s is not a palindrome" % s)
    '''

    '''
    # print k-mers
    s = "ATGCAATTGCGCATCG"
    k = 3
    kmers(s, k)
    '''

    # class exercises
        # print half of the string
        # print alternate characters of a string
        # write a program to concatenate two strings
        # find first occurrence of a character in a string
        # find highest frequency character in a string
        # replace all occurrences of a character with another character
        # trim leading whitespace characters from a string
        # count no of occurrences of a word in a sentence
        # check if two strings are anagrams of each other - use sort function - listen and silent are anagrams, gram and arm are not anagrams



    '''
    # demonstration of list - element search
    l = [1, 2, 8, "Joe", 5]
    # iterate
    for item in l:
        print(item)

    for i in range(len(l)):
        print(l[i])

    # search
    output = 5 in l
    print(output)

    # insert
    l[3] = 4
    print(l)
    '''

    '''
    # demonstration of a dict - element search
    d = {"Rohit":20, "Gill":40}
    # iterate
    for item in d:
        print(item, d[item])

    # search
    output = "Rohit" in d
    print(output)

    # insert
    d["Virat"] = 50
    '''

    '''
    # Map and Lambda.
    # Return double of n
    def addition(n):
        return n + n

    # We double all numbers using map()
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    print(list(result))

    # Double all numbers using map and lambda
    numbers = (1, 2, 3, 4)
    result = map(lambda x: x + x, numbers)
    print(list(result))
    '''



# The __name__ variable is set to __main__ and this statement is true
# The below print statement will not be printed if this file is imported (to use functions defined here) in another program.
if __name__ == "__main__":
    # print("This is the beginning of my program")
    main()
