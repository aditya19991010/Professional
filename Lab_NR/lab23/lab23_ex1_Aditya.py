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
from audioop import reverse
from readline import append_history_file
from traceback import print_tb
from typing import OrderedDict

from Lab_NR.Lab15 import triangle

character_dict = {",":(1,1),".":(1,2),"?":(1,3),"!":(1,4),"A":(2,1),"B":(2,2),"C":(2,3),"D":(3,1),"E":(3,2),"F":(3,3),"G":(4,1),"H":(4,2),"I":(4,3),"J":(5,1),"K":(5,2),"L":(5,3),"M":(6,1),"N":(6,2),"O":(6,3),"P":(7,1),"Q":(7,2),"R":(7,3),"S":(7,4),"T":(8,1),"U":(8,2),"V":(8,3),"W":(9,1),"X":(9,2),"Y":(9,3),"Z":(9,4)}


# character_dict = {1:{1:".",2:",",3:"?",4:"!"},
#                   2:{1:"A",2:"B",3:"C"},
#                   3:{1:"D",2:"E",3:"F"},
#                   4:{1:"G",2:"H",3:"I"},
#                   5:{1:"J",2:"K",3:"L"},
#                   6:{1:"M",2:"N",3:"O"},
#                   7:{1:"P",2:"Q",3:"R",4:"S"},8:{1:"T",2:"U",3:"V"},9:{1:"W",2:"X",3:"Y",4:"Z"},10:" "}
#



string = "Hello! World"

def find_letter(string):
    output = []
    for letter in string:
        for key,value in character_dict.items():
            if letter == key:
                output.append(key)

    return output

print(find_letter(string))








# def write_int_fromstring(string):
#     num_list = []
#     string = str(string.upper())
#     for letters in string:
#         for key, values in (character_dict.items()):
#                 for key_nes, value_nes in (values.items()):
#                     if letters not in value_nes:
#                         continue
#                     else:
#                         num_list.append(key)
#                         num_list.append(key_nes)
#                         break
#                 continue
#             break

# write_int_fromstring(string)
# use yield
