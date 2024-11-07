def calculator(n1,n2,inp_operator):
    try:
        if inp_operator == "+":
            res = lambda n1,n2: n1 + n2
            return print(f"Sum of {n1} and {n2} is {res(n1,n2)}")
        elif inp_operator == "-":
            res = lambda n1,n2: n1 - n2
            return print(f"Substraction of {n1} and {n2} is {res(n1,n2)}")
        elif inp_operator == "/":
            # if n2 == 0:
            #     raise ZeroDivisionError()
            res = lambda n1,n2: n1 / n2
            return print(f"Division of {n1} and {n2} is {res(n1,n2)}")
        elif inp_operator == "*":
            res = lambda n1,n2: n1 * n2
            return print(f"Mutiplication of {n1} and {n2} is {res(n1,n2)}")
        else:
            raise ValueError

    except ValueError as VE:
        print("Bad response, Value error", VE)
    except ZeroDivisionError as ZDE:
        print("Bad response, ZeroDivisionError:", ZDE)

calculator(2,4,"+")
