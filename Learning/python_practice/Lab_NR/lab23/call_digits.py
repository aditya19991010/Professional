num =122
ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
tenth = {1:{0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"forteen",5:"fifteeb",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}, 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

hundredth_pos = num//100
tenth_pos = (num % 100) // 10
one_pos = (num % 10) // 1

str = ""
# case1
if tenth_pos > 1 :
    str = ones.get(str([hundredth_pos])) + "hundred" + tenth.get(int([tenth_pos])) + ones.get(int([one_pos]))

elif tenth_pos == 0:
    str = ones.get(int([hundredth_pos])) + "hundred" + ones.get(int([one_pos]))

elif tenth_pos == 1:
    str = ones.get(int([hundredth_pos])) + "hundred" + tenth.get(int([tenth_pos][one_pos]))

print(str)

if tenth_pos == 0:  # Case 1
    res = print(ones.get(int(hundredth_pos)), "hundred")
    return res
elif tenth == 1:
    x = tenth[tenth_pos][one_pos]
    res = print(ones.get(int(hundredth_pos)), print(x), "hundred")

elif tenth_pos > 1:
    x = tenth[tenth_pos][one_pos]

    tenth_pos == [x for x in range(0, 9)] and one_pos == [x for x in range(0, 9)]:  # case2
    x = tenth.get(int([tenth_pos][one_pos]))
else:
    x = tenth.get(int(tenth_pos))
