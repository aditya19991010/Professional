
    #
    # res = print(ones.get(int(hundredth_pos)), "hundred and", print(int(tenth_pos)), ones.get(int(one_pos)))
    #
    # return res

    if tenth_pos == 0:    #Case 1
        res = print(ones.get(int(hundredth_pos)), "hundred")
        return res
    elif tenth == 1:
        x = tenth[tenth_pos][one_pos]
        res = print(ones.get(int(hundredth_pos)), print(x), "hundred")

    elif tenth_pos > 1:
        x = tenth[tenth_pos][one_pos]


        tenth_pos == [x for x in range(0,9)] and one_pos == [x for x in range(0,9)]: #case2
        x = tenth.get(int([tenth_pos][one_pos]))
    else:
        x = tenth.get(int(tenth_pos))


    return res

call_digits(100)

#
# test digits
# -2
# 0
# 8
# 10
# 18
# 29
# 100
# 409
# 980
# 783
# 1003