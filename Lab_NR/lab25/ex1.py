def checkList(userinput, userindex):
    try:
        print(userinput[userindex])
        # userinput = [x for x in list(userinput)]
        # if userinput[userindex] in userinput:
        #     print(f"The input {userinput[userindex]} is present at index {userindex}")
        # else:
        #     raise IndexError("Index out of range")
        # raise TypeError()
    except IndexError as IE:
        print("Bad response, Index error: ", IE)
    except TypeError as TE:
        print("Bad response, Type error: ", TE)

num_list = [1,2,3,4,5]
string_input = "Hello"
boolean_value = True
checkList(userinput=string_input, userindex=89)
