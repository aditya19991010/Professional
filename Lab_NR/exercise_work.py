#Christmas song
gift_list = {
    1 : "A partridge in a pear tree",
    2 : "Two turtle doves",
    3 : "Three French Hens" ,
    4 : "Four calling birds",
    5: "Five Golden Rings"
}
day_list = {
    1:"first",
    2: "second",
    3:"third",
    4:"fourth",
    5:"fifth"
}
def christmas_song():
    for i in range(1,6):
        print(f"On the {day_list[i]} day of Christmas, I got {gift_list[i]}")

christmas_song()

def christmas_song_recursive():
    total_day = len(day_list.items())
    gifts = ""
    print(f"On the {day_list[1]} day of Christmas, I got {gift_list[1]}")
    for i in range(2,total_day+1):
        gifts +=  "," + gift_list[i]
        print(f"On the {day_list[i]} day of Christmas, I got {gift_list[1]} {gifts}")

christmas_song_recursive()
print("\n\n")

#GCD
def gcd(*args):
    dict_divisor = {}
    for dividend in args:
        divisor_list = []
        quo = dividend
        divisor = 2
        while quo != 1:
            r = quo % divisor
            if r == 0:
                quo = quo // divisor
                divisor_list.append(divisor)
            else:
                divisor += 1
        dict_divisor[dividend] = divisor_list
    common = [set(value) for value in dict_divisor.values()]
    d = set.intersection(*common) if common else set()
    print(f"GCD of {args} is {d}")

gcd(4,6,8)
print("\n\n")


#hash functions
items = ['abcde', 'bcdea', 'cdeba']
def hash(items):
    sum = 0
    for j in range(len(items)):
        item = [x for x in items[j]]
        ord_item = [ord(x) for x in item]
        for i in ord_item:
            position = ord_item.index(i) + 1
            sum += i*position
        print("letters-->",item)
        print("Hash value-->", sum)

hash(items)
print("\n\n")



#dict character

character_dict = {
    ",": (1, 1), ".":(1,1),"?":(1,1,1),"!":(1,1,1,1),
    "A":(2),"B":(2,2),"C":(2,2,2),
    "D":(3),"E":(3,3),"F":(3,3,3),
    "G":(4),"H":(4,4),"I":(4,4,4),
    "J":(5),"K":(5,5),"L":(5,5,5),
    "M":(6),"N":(6,6),"O":(6,6,6),
    "P":(7),"Q":(7,7),"R":(7,7,7),"S":(7,7,7,7),
    "T":(8),"U":(8,8),"V":(8,8,8),
    "W":(9),"X":(9,9),"Y":(9,9,9),"Z":(9,9,9,9),
    " " : (10)}


def find_letter(string):
    charac_list = [x for x in string.upper()]
    num_list = str([character_dict[i] for i in charac_list])

    return print(num_list)

string = "Hello, World!"
find_letter(string)


