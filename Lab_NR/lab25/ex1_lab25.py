def checkList(userinput, userindex):
    userinput_fmt = ""
    if userinput.isalpha:
        userinput_fmt = userinput_fmt.isalpha()
        userinput = [list(x) for x in userinput ]

    elif userinput[0].is_integer():
        userinput = [x for x in userinput ]
    except IndexError as IE:
        print("Bad response, Value error: ", IE)
    elif userinput.isalpha():
        userinput = [list(x) for x in userinput ]
        try:
            if userinput[userindex] in userinput:
                print(f"The input {userinput[userindex]} is present at index {userindex}")
            else:
                raise IndexError("Index out of range")
    else:

else:
raise TypeError("TypeError")

num_list = [1,2,3,4,5]
string_input = "Hello"
checkList(userinput=num_list, userindex=3)



# agetoolowerror(exception)

