character_dict = {
    1: {1: ".", 2: ",", 3: "?", 4: "!"},
    2: {1: "A", 2: "B", 3: "C"},
    3: {1: "D", 2: "E", 3: "F"},
    4: {1: "G", 2: "H", 3: "I"},
    5: {1: "J", 2: "K", 3: "L"},
    6: {1: "M", 2: "N", 3: "O"},
    7: {1: "P", 2: "Q", 3: "R", 4: "S"},
    8: {1: "T", 2: "U", 3: "V"},
    9: {1: "W", 2: "X", 3: "Y", 4: "Z"},
    10: " "
}

string = "Hello! World"

def write_int_from_string(string):
    num_list = []
    string = str(string.upper())
    for letter in string:
        found = False
        for key, values in character_dict.items():
            if isinstance(values, dict):  # Check if the value is a nested dictionary
                for key_nes, value_nes in values.items():
                    if letter == value_nes:
                        num_list.append(key)
                        num_list.append(key_nes)
                        found = True
                        break  # Break out of the inner loop
            elif letter == values:  # Handle spaces or non-dictionary entries
                num_list.append(key)
                found = True
                break  # Break out of the loop if found
            if found:
                break  # Break the outer loop if found
    return num_list

# Example usage
num_list = write_int_from_string(string)
print(num_list)
