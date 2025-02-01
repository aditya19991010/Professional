#On some basic cell phones, text messages can be sent using the numeric keypad.
# Because each key has multiple letters associated with it, multiple key presses are needed
# for most letters. Pressing the number once generates the first letter on the key. Pressing
# the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character listed for
# the key.
#
# Write a program that displays the key presses that must be made to enter a text
# message read from the user. Construct a dictionary that maps from each letter or symbol
# to the key presses or the reverse. Then use the dictionary to generate and display the
# presses for the user’s message. For example, if the user enters Hello, World! then your
# program should output 4433555555666110966677755531111.

character_dict = {
    ",": (1, 1), ".":(1,1),"?":(1,1,1),"!":(1,1,1,1),
    "A":(2,),"B":(2,2),"C":(2,2,2),
    "D":(3,),"E":(3,3),"F":(3,3,3),
    "G":(4,),"H":(4,4),"I":(4,4,4),
    "J":(5,),"K":(5,5),"L":(5,5,5),
    "M":(6,),"N":(6,6),"O":(6,6,6),
    "P":(7,),"Q":(7,7),"R":(7,7,7),"S":(7,7,7,7),
    "T":(8,),"U":(8,8),"V":(8,8,8),
    "W":(9,),"X":(9,9),"Y":(9,9,9),"Z":(9,9,9,9),
    " " : (10,)}





string = "Hello, World!"

def find_letter(string):
    output = []
    for letter in string.upper():
        for key,value in character_dict.items():
            if letter == key:
                output.append(value)
    list_of_tuples = output
    list_num = [items for x in list_of_tuples for items in x]
    map_items = map(str, list_num) #converting list items into string format
    digits = " ".join(map_items)
    return digits


list_of_tuples = find_letter(string)
print(list_of_tuples)
