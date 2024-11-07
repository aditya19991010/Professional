def checkList(userinput, userindex):
    try:
        print(userinput[userindex])
    except IndexError as IE:
        print("Bad response, Index error: ", IE)
    except TypeError as TE:
        print("Bad response, Type error: ", TE)

num_list = [1,2,3,4,5]
string_input = "Hello"
boolean_value = True
checkList(userinput=boolean_value, userindex=89)
