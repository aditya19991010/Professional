class Quadrilateral():
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def isSquare(self):
        equal_sides = False
        if self.side1 == self.side2 == self.side3 == self.side4:
            equal_sides = True
            print("Quadrilateral is a square :", equal_sides)
        else:
            print("Quadrilateral is a square :", equal_sides)

    def isrectangle(self):
        opposite_side_equal = False
        if self.side1 == self.side3 == self.side2 == self.side4:
            opposite_side_equal = False
            print("Quadrilateral is not a rectangle  :", opposite_side_equal)
        elif self.side1 == self.side3 and self.side2 == self.side4:
            opposite_side_equal = True
            print("Quadrilateral is a rectangle :", opposite_side_equal)
        else:
            print("Quadrilateral is a not rectangle :", opposite_side_equal)

print("a. All sides being different")

shape = Quadrilateral(2,3,2,3)
shape.isSquare()
shape.isrectangle()
print("\nb. Opposite sides being different")
shape = Quadrilateral(4,3,2,5)
shape.isSquare()
shape.isrectangle()
print("\nc. All side being the same")

shape = Quadrilateral(4,4,4,4)
shape.isSquare()
shape.isrectangle()


class Square(Quadrilateral):
    def __init__(self,side1):
        super().__init__(side1, side1, side1, side1)
        self.side1 = side1
    def getArea(self):
        return print("Area of the square is: ",self.side1**2)

class Rectangle(Quadrilateral):
    def __init__(self, side1, side2):
        super().__init__(side1, side2, side1, side2)
        self.side1 = side1
        self.side2 = side2

    def getArea(self):
        return print("Area of the rectangle is: ",self.side1*self.side2)

Area_square = Square(10)
Area_square.getArea()
Area_rectangle = Rectangle(8,10)
Area_rectangle.getArea()
