# 1. convert farenheit to celcius

def Faren_to_celc(F):
    c =  ( F - 32 ) * ( 5/9)
    return (c)

F = input("Enter a value:\n")
c = Faren_to_celc(F)
print(f"The value after conversion in {c}")


# 2. check if the number is even or odd

def check_odd_even(num):
    if num == 0 :
        result =  print("please enter the natural number")
    elif (num % 2 == 0) :
        result = print("This is an even number")
    elif num %2 != 0 :
        result = print("This is an odd number")
    return (result)


num = int(input("Enter a number:\n"))
result = check_odd_even(num)


# 3. check if a given string is palindrome or note
#     enter a string
#     create a list of alphabets
#     reverse the list based on index and save it in a list
#     check if alphabets in both the strings are same in both indexes

def check_palindrome():
    query = list("Aditya")
    reverse_query = list(reversed(query))
    for i in range(len(reverse_query)):
        if query[i] == reverse_query[i]:
            print("This sequence is a palindrome sequence")
        else:
            print("This is not a palindrome")
check_palindrome()


# 4.print 10 terms of fibonacci series
