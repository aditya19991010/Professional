#call digits



def call_digits(num):
    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tenth = {1:{0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"forteen",5:"fifteeb",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}, 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    hundredth_pos = int(num//100)
    tenth_pos = int((num % 100) // 10)
    one_pos = int((num % 10) // 1)

    if num <0 :
        res = print("error, Please Be +ve!")
        return res

    elif len(str(num)) == 3 :
        if tenth_pos > 1 and one_pos == 0 :
            # case num at tenth place is  > 1
            res = print(ones[hundredth_pos], "hundred","and", tenth[tenth_pos])
            return res
        if tenth_pos > 1:
            #case num at tenth place is  > 1
            res = print(ones[hundredth_pos] , "hundred" ,  "and", tenth[tenth_pos] , ones[one_pos])
            return res
            #case num at tenth and ones place is zero
        if tenth_pos == 0 and one_pos == 0:
            res = print(ones[hundredth_pos] , "hundred")
            return res
            #case num at tenth place is zero
        if tenth_pos ==0:
            res = print(ones[hundredth_pos] , "hundred" , "and", ones[one_pos])
            return res
            #case num at ones place is zero
        if one_pos == 0 :
            res = print(ones[hundredth_pos] , "hundred" ,  "and", tenth[tenth_pos])
            return res
           #case num at tenth place is one
        if tenth_pos == 1:
            res = print(ones[hundredth_pos] , "hundred" ,  "and", tenth[tenth_pos][one_pos])
            return res
    if len(str(num)) == 1 :
        res = print(ones[one_pos])
        return res
    elif len(str(num)) == 2 :
        if tenth_pos == 1:
            res = print(tenth[tenth_pos][one_pos])
            return res
        elif tenth_pos > 1:
            #case num at tenth place is  > 1
            res = print(tenth[tenth_pos] , ones[one_pos])
            return res
    else:
        print("error")

call_digits(10)

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