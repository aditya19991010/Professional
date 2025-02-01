# A. Write a function that takes age as input and prints the age in the next 10 years. If the
# age entered is negative, raise a ValueError(“Age cannot be negative”). Call the above
# function with negative input within the try block. If an exception occurs, print the error.


def age_calc():
    year = 2024
    n = 10
    try:
        age = int(input("Enter age: ")) # Throws an error and break the code, then enter into the except block
        while n > 1:
            if age < 1:
                raise ValueError("Age cannot be negative")
            elif age > 1:
                age +=1
                year += 1
                print(f"Age in {year} will be {age}.")
                n -= 1
            else:
                raise Exception("Please enter a Positive integer.")
    except ValueError as verr:
        print("Bad response, Value error: ", verr)
    except Exception as err:
        print("Bad response: ", err)

age_calc()


# B. Write a function that takes a number and divides 100 by that number within try. If the
# number entered is 0 or negative, catch the corresponding exceptions and print them.

def num_division():
    num = int(input("Please enter a positive whole number: "))
    try:
        if num == 0 :
            raise Exception("Please a number greater than zero.")
        elif num  < 1 :
            raise Exception("Please a positive num.")
        elif num > 1 :
            res = num/100
            print(res)
    except Exception as exp:
        print(f"Bad response: {exp}")


num_division()