# 1. Write a python script to convert a non negative decimal number to
# binary representation without using any libraries


def convert_dec_binary():
    res = ""
    num = int(input("Enter a non negative decimal number: "))
    while num>1 :
        rd = num//2
        qt = num%2
        res = str(qt) + res
        num = rd
    res = str(rd) + res
    print(res)

# convert_dec_binary()

# 2. Write a python script to produce a Caesar cipher - take a message in
# English alphabet - plaintext and a shift integer. Each character should
# be replaced by the character + shift . Let the non alphabetic
# characters be represented as they are

text = ""
def cesar_shift(text):
    shift_int = int(input("Enter a shift integer: "))
    output = ""
    for charac in text:
        if "a" <= charac <= "z":
            temp=ord(charac) + shift_int
            output += chr(temp)
        if "A" <= charac <= "Z":
            output += charac
    print("Caesar shift output : ",output)

text = "AdityA"
cesar_shift(text)



# 3. Write a Python script to get the co-ordinates of several points in a
# polygon and print the perimeter of the p polygon. The points should
# be obtained in loops until a blank line is entered.

from math import sqrt
# d=√((x2 – x1)² + (y2 – y1)²)

def coordinates(x,y):
    perimeter = x + y
    x = []
    y = []
    d = sqrt((x2-x1)**2 + ())




# 4. Write a python script to check if a given string is a palindrome or not.

# 5. Write a python script that takes 8 bits at a time as input. If the no. of
# 1s in the byte is even, it prints the parity bit as 0, else it prints it as 1.


