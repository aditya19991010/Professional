#ex2
# A. Write a function greet() that takes an input message as argument and prints it. Write a
# decorative function upper_case_greet() that converts the argument to greet() to upper
# case .


def upper_case_greet(func):
    def repeat_greet():
        x = func()
        n_times = int(input("Enter an intger: "))
        print(x.upper())
        res = x*n_times
        print(res)
    return repeat_greet


@upper_case_greet
def greet():
    inp = input("Enter any greeting message: ")
    return str(inp)

greet()

# B. Use another decorator function repeat(n_times) that takes an argument integer . It
# should call the function greet() n_times.


