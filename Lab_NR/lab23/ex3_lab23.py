# A. Create two functions AddNumbers(x,y) and SubtractNumbers(x,y) that add/subtract
# the two numbers respectively. Create a function OperateNumbers that takes
# AddNumbers / SubtractNumbers as argument and invokes the function passed as
# argument with default values.
from pydoc import replace
from time import process_time_ns


def AddNumbers(x,y):
    res = x + y
    return print(f"Addition of {x} and {y} is {res}")

def SubtractNumbers(x,y):
    res = x-y
    return print(f"Subtraction of {x} and {y} is {res}")


def OperateNumbers(func,a,b):
    func(a,b)
    return


OperateNumbers(AddNumbers,1010,1202)
OperateNumbers(SubtractNumbers,1010,800)

# B. Repeat the above for the operations on strings (ConcatenateStrings(str1, str2) and
# ReplaceWord(str1, str2=”” and OperateStrings(func) )

str1 = "Hello! "
str2 = "World"
def ConcatenateStrings(str1,str2):
    return print(str1+str2,"\n")

def ReplaceWord(str1,str2=""):
    changed = str1.replace(str1,str2)
    return print(changed,"\n")

def OperateStrings(func,a,b):
    return func(a,b)

print("Concatenate string , str1 and str2 ---->")
OperateStrings(ConcatenateStrings,str1,str2)

print("Replacing str1 = 'Hello!' with str2 = 'World'---->")
OperateStrings(ReplaceWord,str1,str2)
