#2 Create a dictionary of friends with three keys {“name”,”age”,”city”}. Create a lambda
# function on a dictionary with the key age. Use this function with sorted() to sort the
# dictionary by age

dict = [
    {"name":"Anshul", "age": 44, "city" : "Jaipur"},
    {"name": "Rakesh", "age": 23, "city" : "Pune"},
    {"name": "Gaurav", "age": 56, "city" : "Mumbai"}]

print(f"Dictionary before sorting: ",dict)
# print(dict.keys())
def sorted_by_key(dict, key_dict):
    sorting_dict = lambda x : x[key_dict]
    dict_sorted = sorted(dict, key=sorting_dict)
    return dict_sorted

sorted_dict = sorted_by_key(dict, "age")
print(f"Dictionary after sorting: ", sorted_dict)