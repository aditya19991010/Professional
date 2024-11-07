'''XML  -
<XML>
    <ELEMENTS ...... /ELEMENT>
</XML>
'''

import csv

players = [
    ['Rohi', 'Sharma' ],
    ['Virat',  'Kohli'],
    ['Viraj', 'Nataraj']
]

#writing the file
with open('player.txt', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerow(players)

#Reading the file
with open('player.txt', 'rt') as fin:
    cin = csv.reader(fin)
    p = [row for row in cin]
    print(p)

#writing dictionary
p1_morse_dict = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":".-.",
              "L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--",
              "Z":"--..",0:"----",1:".----",2:"..---",3:"...---",4:"....-",5:".....",6:"-....",7:"--...",8:"---..",9:"----."}


#use Dictwrite for reading dictionary

#XML
'''
    <Countries> <--Tag
        <Country>  
            <State> "MP" #element </State>
        </Country>
    </Countries>
'''

# xml.dom #for performance
# xml.sax

#JSON
# follow key value = dictionary notation
import json

menu = \
    {"breakfast": {
        "hours":"7-11", "item":{
            "breakfast burritos":"$6",
            "pancakes":"$4"
        }
    }
    }

menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json) #turns JSON string back into a Python
print(menu2)

#serialze by using pickle
#Saving Data structure to a file called serializing
#for storing data in intermediate steps

import pickle
import datetime

now1  = datetime.date(2024,12,1)
print(now1)
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now2)


#reading excel file - use xlrd library
#HDF5 - h5py, PyTables


