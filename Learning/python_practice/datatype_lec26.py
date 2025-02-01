#Datatypes
# 4 different datatypes
# 1. Boolean
# 2. Float
# 3. Integer
# 4. String


# correc it
def sum_consecutive(a):
    res = 0
    while a == 0 :
        a -= 1
    res = res + a
    result = print(f"Sum of numbers is : {res}" )
    return result


def main():
    a = int(input("Enter a number"))
    res = sum_consecutive(a)

if __name__== '__main__':
    main()

# Datatypes
print(type('abs'))
print(type(0.62))
print(type(6))

print(5/2)
print(5//2) #truncates the integer
print(5//2)

def Datatypes():
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

    i = 'IBAB'
    p = int(i)
    print(p) # error . program build to take only interger value
    print(type(p))

    a = 10 **100
    print(a)

#def String_operations():

bottles = 99
base = ''
base = "The score is :"
base += 'hi'
print(base)

palindrome = 'A man , \nA plan, \nA:\nPanama.'
print(palindrome)
print('a\tbc')
print('ab\tc')
print('abc\t')

palindrome = '\"A man , \nA plan, \nA:\nPanama\".'
print(palindrome)


start = 'Hello\t' *100 + '\n'
middle = 'Hey\t' * 100 + '\n'
end = 'Goodbye.'
print(start + middle + end )