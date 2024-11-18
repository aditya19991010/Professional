
import json
from fileinput import filename

from matplotlib.font_manager import json_load

input_data = \
[
    {
        "player_name": "Shubham",
        "player_email": "shubham@abc.org",
        "player_score": 45,
        "man_of_the_match": False
    },
    {
        "player_name": "Rohit",
        "player_email": "rohit@abc.org",
        "player_score": 75,
        "man_of_the_match": False
    },
    {
        "player_name": "Virat",
        "player_email": "virat@abc.org",
        "player_score": 100,
        "man_of_the_match": False
    }
]



def JSONProcessor(file_name, input_data):
    js_dump = json.dumps(input_data)
    with open(file_name, 'w') as file:
        file.write(js_dump)

    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
    print(json_data)


file = "/home/group_nithya01/PycharmProjects/Work_update/Lab_NR/lab27/1MB.json"
file_name = "temp.json"
JSONProcessor(file_name, input_data)


def set_MOM(file_name):
    with open(file_name, 'w') as file:
        js_data = json.dumps(file)

    MOM= ""
    for item in js_data:
        for key,value in item.items():
            if item["player_score"] > 
