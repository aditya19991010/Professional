#Slicing

'''
In python everything is considered as an object. Therefore, a function is required to add in a variable followed by '.' . to access to property
'''



#print(S[:]) -> This option prints entire string
# print(S[-1] )
# S[start : end : step] -> used in all DSA
# print("The index of string is\t")
# for i in range(length):
#     print(i, end=' ' )
# print("\n")

S= "Welcome to python programming"

def strings_func():
    #slicing upto 4th index
    print(S[5:])

    print(S[:5])

    print("NEGATIVE SLICING", S[-3:])
    print(S[:-5])
    print(S[0:9:2]) #steps to the second incoming number
    print(S[2:5])
    print("REVERSE", S[::-1])
    print("End at -3 index and starting from 18th index: ", S[18:-3])
    print("Stepping with 7 steps at a time : ", S[::7]) #Starts from zeroth position
    print("started from -1 and stepping -1 at a time :", S[-1::-1])
    print(S[-130:])

def stringops():
    length = len(S)
    print("Length of the string: ", length)

    tokens = S.split(' ') # split at the place where it finds space ' '.
    print(tokens)

    s1 = ' '.join(tokens) #join the tokens at the place where it finds ' '.
    print(s1)

    s2 = S.startswith("Welcome") # check if the string starts with the specific words
    print(s2)

    s3 = S.endswith(",Aditya")
    print(s3)

    #Check word occurrence
    word = "Aditya"
    s4 = S.find(word)
    print(s4)

    word = "to"
    s5 = S.rfind(word)
    print(s5)

    # count
    s6 = S.count(word)
    print("Count of 'to' is/are : " , s6)

    # checking the input
    setup = "               the white duck in the park is playing around the bush...        "
    p1 = setup.strip('.')
    print(p1)

    print(setup.title())
    print("SWAPCASE USAGE: ", setup.swapcase())
    print(setup.center(5))
    print(setup.ljust(30))

    ##String are immutable means once you allocated it is not changeable

    # p = "Hello"
    # p[2] = 'k'


def main():
    S= "Welcome to python programming"
    return stringops()
    #return strings_func()

if __name__=='__main__':
    main()



