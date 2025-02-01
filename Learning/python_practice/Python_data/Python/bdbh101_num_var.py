# All examples are taken from Introduction to Python - Bill Lubanovic - Thanks!
def datatypes():
    # basic built-in data types - integers, floats, boolean and strings

    # assignment
    a = 7
    print(a)
    b = a
    print(b)

    # In Python, type and class mean same thing
    print(type(a))
    print(type(b))
    print(type(99.8))
    print(type('abc'))

    # variable names can only contain these characters
    # lowercase letters (a through z)
    # uppercase letters (A through Z)
    # digits (0 to 9)
    # underscore (_)

    # names cannot begin with digits
    # Python treats names that begin with underscore (_) in special ways
    # do not use these reserved words
    # False      class      finally    is         return None       continue   for
    # lambda     try True       def        from       nonlocal   while and        del
    # global     not        with as         elif       if         or         yield assert     else
    # import     pass break      except     in         raise

    # numbers
    # supported operators
    # + (addition), - (subtraction), * (multiplication), / (floating point division)
    print(5/2)
    # // (integer truncating division) 5 // 2 = 2
    print(5 // 2)
    # % (modulus - remainder)
    print(5 % 2)
    # ** (exponentiation)
    print(2 ** 5)
    # to specify a negative number, insert - before the number
    n = -3
    print(n)
    # assignment does not copy a value, it just attaches a name
    a = 100
    temp = a
    print(temp)
    temp = 25
    print(temp)

    # combine arithmetic operator with assignment
    a = 95
    a -= 3
    print(a)
    a /= 3
    print(a)
    a = 13
    a //= 4
    print(a)

    # get both the (truncated) quotient and remainder at once
    print(divmod(9,5))

    # precedence rules - refer to Appendix F in Introduction to Python book
    # Always use ( and ) explicitly in your programs and not rely on precedence rules

    # In Python, you can express literal integers in three bases
    # 0b or 0B for binary (base 2)
    # 0o or 0O for octal (base 8)
    # 0x or 0X for hexa (base 16)
    d = 20
    print(d)
    b = 0b10100
    print(b)
    o = 0o24
    print(o)
    h =0x14
    print(h)

    # type conversions
    a = int(True)
    print(a)
    b = int(False)
    print(b)
    c = int(98.6)
    print(c)
    d = 1.58e4
    print(d)
    print(type(d))
    e = int(d)
    print(type(e))
    s = '99'
    print(type(s))
    i = int(s)
    print(i)
    print(type(i))
    print(int('-23'))
    # print(int("hello"))
    # int()  will make integers from floats or stings of digits, but won't handle strings containing decimal points
    # s = int('98.4') # exception
    print(3 + 4.5)
    print(True + 2)
    print(False + 2)
    # In Python 3 integers can be of any size, unlike Python 2 which is 32-bits
    a = 10 ** 100 # googol and was the original name of Google
    print(a)
    # floats
    print(float(True))
    print(float(False))
    print(float(98))
    print(float('99'))
    print(float('98.6'))
    print(float('-1.5'))
    print(float('1.0e4'))


def stringops():

    s = "Welcome to BDBH101 Python Programming"
    p = 'Welcome to BDBH101 Python Programming'
    q = "'Nay,' said the naysayer."
    r = 'The rare double quote in captivity: ".'
    t = 'A "two by four" is actually 1 1⁄2" × 3 1⁄2".'
    u = "'There's the man that shot my paw!' cried the limping hound."
    v = '''Boom!'''
    w = """Bam"""
    # triple quotes are used to create multiline strings
    poem = '''There was a Young Lady of Norway, 
            Who casually sat in a doorway; 
            When the door squeezed her flat, 
            She exclaimed, "What of that?" 
            This courageous Young Lady of Norway.'''
    print(poem)

    e = ''  # empty string

    # build a string from other string
    bottles = 99
    base = ''
    base += 'current inventory: '
    base += str(bottles)
    print(base)

    # convert Python data types to string
    si = str(98.6)
    print(si, ',', type(si))
    sf = str(1.0e4)
    sb = str(True)
    print(type(sb))

    # escape
    palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
    print(palindrome)
    print('\tabc')
    print('a\tbc')
    print('ab\tc')
    print('abc\t')

    testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
    print(testimony)
    fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
    print(fact)
    speech = 'Today we honor our friend, the backslash: \\.'
    print(speech)

    # combine literal string
    c = 'Release the kraken! ' + 'No, wait!'
    print(c)
    a = 'Duck.'
    b = a
    c = 'Grey Duck!'
    d =  a + b + c
    print(d)

    # duplicate with *
    start = 'Hello  ' * 4 + '\n'
    print(start)
    middle = 'Hey ' * 3 + '\n'
    end = 'Goodbye.'
    print(start + start + middle + end)

    # extract a character with []
    # The first (leftmost) offset is 0, the next is 1, and so on. The last (rightmost) offset can be specified with –1
    print("The original string is : ", s)
    print(s[0], s[3])
    print(s[-1])
    print(s[-2])


    # strings are immutable
    # s[0] = 'a' # error
    # use replace
    name = 'Henny'
    newname = name.replace('H', 'P')
    print(newname)

    # string concatenation
    new_word = s + ' located in Bangalore'
    print(new_word)

    # slicing with [start:end:step]
    print(s[:]) # entire sequence
    print(s[5:]) # starting from offset 5 till the end
    print(s[:5]) # from the beginning to the end offset -1
    print(s[2:5]) # from start offset 2 the end offset 5 - 1
    print(s[0:9:2]) # start offset to the end offset -1, skipping characters by 2
    print(s[-3:]) # last 3 characters
    print(s[::-1]) # prints in revere order
    print(s[18:-3]) # we go from offset 18 to the fourth before the end
    print(s[-6:-2]) # we extract from 6 before the end to 3 before the end:
    print(s[::7]) # From the start to the end, in steps of 7 characters:
    print(s[4:20:3]) # From offset 4 to 19, by 3:
    print(s[19::4]) # From offset 19 to the end, by 4
    print(s[:21:5]) # From the start to offset 20 by 5:
    # step backward
    print(s[-1::-1]) # This starts at the end and ends at the start, skipping nothing
    print(s[::-1]) # same result as above
    # A slice offset earlier than the beginning of a string is treated as 0, and one after the end is treated as-1
    print(s[-150:]) # From 150 before the end to the end:
    print(s[-1:])
    print(s[-51:-50])
    print(s[:70])
    print(s[70:71])

    # string length
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

    # Are all of the characters in the poem either letters or numbers?
    print(s.isalnum())

    # case and alignment
    setup = 'a duck goes into a bar...'
    nodots = setup.strip('.')
    print(nodots)
    # capitalize
    print(setup.capitalize())
    # capitalize all words
    print(setup.title())
    # convert all characters to uppercase
    print(setup.upper())
    # convert all characters to lowercase
    print(setup.lower())
    # Swap upper- and lowercase:
    print(setup.swapcase())
    # alignment
    # Center the string within 30 spaces:
    print(setup.center(30))
    # Left justify:
    setup.ljust(30)
    # Right justify:
    setup.rjust(30)
    # substitute with replace
    print(setup.replace('duck', 'marmoset'))
    print(setup.replace('a ', 'a famous ', 100))
    print( setup.replace('a', 'a famous', 100))


def palindrome(s):
    palin = True
    if (s == s[::-1]):
        palin = True
    else:
        palin = False

    return (palin)

def kmers(s, k):
    str_length = len(s)
    for i in range(0, str_length-k+1):
        kmer = s[i:i+k]
        print(kmer)

def main():

    # datatypes()
    # stringops()

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


if __name__ == "__main__":
    # print("This is the beginning of my program")
    main()


# class exercises
# 1. sum of squares of first N numbers
# 2. convert the decimal number D into binary.
# 3. write a function that computes the number of 1s in a binary representation of a decimal number, N.
# 4. convert the binary number B into decimal.
# 5. write a function that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.
# 6. write a function to check if a given number, N, is prime or not
# 7. print individual digits of a number, N.

# class exercises - strings
# 8. print half of the string
# 9. print alternate characters of a string
# 10. write a program to concatenate two strings
# 11. find first occurrence of a character in a string
# 12. find highest frequency character in a string
# 13. replace all occurrences of a character with another character
# 14. trim leading whitespace characters from a string
# 15. count no of occurrences of a word in a sentence
# 16. check if two strings are anagrams of each other - use sort function - listen and silent are anagrams, gram and arm are not anagrams