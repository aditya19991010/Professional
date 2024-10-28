# A. Create a global variable x and assign it to an integer. Create a local variable z inside a
# function checkNameSpaces() and assign it to another value. Change the value of global
# variable x inside checkNameSpace(). Print the values of local and global variables using
# global() and local() calls. Observe the dictionary output of globals to look for x.
import time

x = 1
print(f"Printing x and global var --> x = {x}\n\nGlobal variable\n{globals()}")

print("\nChanging variable type..")
time.sleep(0.2)
def checkNameSpaces():
    z = 33
    global x
    x = 12
    return print(f"\nPrinting value of (z =local variable,x) variable --> {(z, x)}")

checkNameSpaces()

