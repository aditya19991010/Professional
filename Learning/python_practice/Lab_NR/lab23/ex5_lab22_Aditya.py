#5 Create a lambda function as a variable called reverse_string that reverses the given
# string. Create a dictionary of name-value pairs. Use the reverse_string variable to check
# if the name and value pairs are/are not the reverse of each other and print True/False for
# the corresponding key

def reverse_string(dict_1):
    reverse_string = lambda x: x[::-1]
    for key,value in (dict_1.items()):
        if (reverse_string(key)==value):
            print(key, True)
        else:
            print(key, False)

dict_1 = {"hello":"olleh", "naman":"naman", "Python":"java", "dalad":"dalad"}

reverse_string(dict_1)