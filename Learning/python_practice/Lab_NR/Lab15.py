

#2. Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your
# program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of
# sides outside of this range is entered then your program should display an appropriate error message

dict_shapes = {3:"triangle", 4:"rectangle",5: "pentagon", 6:"hexagon",7:"heptagon",8:"octagon", 9:"nonagon", 10:"decagon"}

# sides = input("Enter number of side: ")
sides =3
def predict_sides(sides):
    sides = int(sides)
    print(f"You have entered {sides}.")
    if sides > 10 or sides < 3:
        output = print("Error, Please enter a number between 3-10.")
        return output
    else:
        for key,value in dict_shapes.items():
            if key == sides:
                output = print(f"The matching shape is {value} with the {key} sides.")
                return output
predict_sides(sides)


#Create a program that reads the name of a month from the user as a string. Then your program should
# display the number of days in that month. Display “28 or 29 days” for February .

calender_dict = {"January" : 31, "February": "29 or 28", "March" : 31, "April":30, "May" : 31, "June":30, "July" : 31, "August" : 31, "September":30, "October" : 31, "November":30, "December" : 31}

def month_name():
    month = input(f'''Please enter name of month from this list \n {list(calender_dict.keys())} \n : ''')
    month = str(month)
    for key,value in calender_dict.items():
        if month == key:
            print(f"The number of days in the month of {key} are {value}.")

# month_name()

#4. A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 3
# sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the
# same length, and a third side that is a different length. If all of the sides have different lengths then the
# triangle is scalene. Write a program that reads the lengths of 3 sides of a triangle from the user.Display a
# message indicating the type of the triangle.

def triangle(a,b,c):
    if a==b or  b==c or a==c:
        print("This is an isoceles triangle")
    elif a==b==c:
        print("This is an equilateral triangle")
    elif a!=b!=c:
        print("This is an scalene triangle")
    else:
        print("error")

triangle(3,3,5)


##A bakery sells loaves of bread for Rs. 25.50 each. Day old bread is discounted by 60 percent. Write a
# program that begins by reading the number of loaves of day old bread being purchased from the user.
# Then your program should display the regular price for the bread, the discount because it is a day old,
# and the total price. All of the values should be displayed using two decimal places, and the decimal points
# in allof the numbers should be aligned when reasonable values are entered by the user.


