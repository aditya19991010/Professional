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
