str1 = "abcdef"
str2 = "bcdefa"
str3 = "cdefab"

sum_str = [ord(j) for j in str1]
total_1 = sum(sum_str)
print(total_1)
print(total_1%2069)