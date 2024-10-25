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

def create_lookup_dict(char_dict):
    """Create a reverse lookup dictionary for efficient access."""
    lookup = {}
    for key, values in char_dict.items():
        if isinstance(values, dict):
            for sub_key, value in values.items():
                lookup[value] = (key, sub_key)
        else:
            lookup[values] = (key,)
    return lookup

def write_int_from_string(string, lookup):
    """Convert a string to its corresponding numeric representation."""
    return [lookup[letter] for letter in string.upper() if letter in lookup]

# Create a lookup dictionary for faster access
lookup_dict = create_lookup_dict(character_dict)

# Example usage
string = "Hello! World"
num_list = write_int_from_string(string, lookup_dict)

# Flatten the list of tuples into a single list
flattened_num_list = [num for pair in num_list for num in pair]
print(flattened_num_list)
