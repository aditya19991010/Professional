

def main():
    # everything in Python, from numbers to modules, is an object
    # an object contains both data (variables called attributes) and code (functions, called methods)
    # an object refers to an unique instance of a class

    class person():
        def __init__(self, name):   # init is like a constructor and initializes a new object from this class
            self.name = name

    player = person("Sachin")
    print(player.name)


    ### inheritance
    # creating a new class from an existing class but with some additions or changes.
    # It’s an excellent way to reuse code.
    # You define only what you need to add or change in the new class, and this overrides
    # the behavior of the old class. The original class is called a parent, superclass, or base
    # class; the new class is called a child, subclass, or derived class. These terms are inter‐
    # changeable in object-oriented programming.

    class player():
        def display(self):
            print("The person is a player")

    class cricket_player(player):
        def display(self):
            print("The person is a cricket player")

        def matches(self):
            print("The person has played 100 matches")

    p = player()
    p.display()
    c = cricket_player()
    c.display()
    c.matches()
    # p.matches()  - ERROR


    ### invoking parent methods
    class Person():
        def __init__(self, name):
            self.name = name

    # When you define an __init__() method for your class, you’re replacing the
    # __init__() method of its parent class, and the latter is not called automatically any‐
    # more. As a result, we need to call it explicitly.
    class EmailPerson(Person):
        def __init__(self, name, email):
            super().__init__(name)
            self.email = email

    sachin = EmailPerson("Sachin Tendulkar", "sachin@bcci.in")
    print(sachin.name)
    print(sachin.email)


    ### Getter and setter
    class Player_Hidden_Name():
        def __init__(self, input_name):
            self.__name = input_name  # two underscores signify hidden variable - just a convention

        @property
        def name(self):
            print('inside the getter')
            return self.__name

        @name.setter
        def name(self, input_name):
            print('inside the setter')
            self.__name = input_name

    p = Player_Hidden_Name("sachin")
    print(p.name)
    p.name = "Tendulkar"
    print(p.name)

    # another example
    class Circle():
        def __init__(self, radius):
            self.radius = radius

        @property
        def diameter(self):
            return 2 * self.radius

    c = Circle(5)
    print(c.diameter)


    # method types @classmethod and @staticmethod
    from datetime import date

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        # a class method to create a Person object by birth year.
        @classmethod
        def fromBirthYear(cls, name, year):
            return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.
        @staticmethod
        def isAdult(age):
            return age > 18

    person1 = Person('mayank', 21)
    person2 = Person.fromBirthYear('mayank', 1996)

    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.isAdult(22))

    class Player():
        count = 0
        def __init__(self):
            Player.count += 1

        def exclaim(self):
            print("I'm a Player!")

        @classmethod
        def kids(cls):
            print("Player has", cls.count, "little objects.")

        @staticmethod
        def about():
            return("This class is about players")

    sachin = Player()
    rohit = Player()
    virat = Player()
    Player.kids()
    print(Player.about())


    ### Polymorphism
    class Player():
        def __init__(self, person, words):
            self.person = person
            self.words = words

        def who(self):
            return self.person

        def says(self):
            return self.words + '.'

    class Batsman(Player):
        def says(self):
            return self.words + 'batsman'

    class Bowler(Player):
        def says(self):
            return self.words + 'bowler'

    p = Player('Sachin', "I'm a player")
    print(p.who(), 'says:', p.says())
    p1 = Batsman('Rohit', "I'm a ")
    print(p1.who(), 'says:', p1.says())
    p2 = Bowler('Jadeja', "I'm a ")
    print(p1.who(), 'says:', p2.says())


    ### Magic methods
    class Word():
        def __init__(self, text):
            self.text = text

        def __eq__(self, word2):
            return self.text.lower() == word2.text.lower()

    first = Word('ha')
    second = Word('HA')
    third = Word('eh')
    print(first == second)
    print(first == third)
    print(first)
    # make it pretty with __str__ and __repr__
    class Word():
        def __init__(self, text):
            self.text = text

        def __eq__(self, word2):
            return self.text.lower() == word2.text.lower()

        def __str__(self):
            return self.text

        def __repr__(self):
            return 'Word("' + self.text  + '")'

    first = Word('ha')
    first  # # uses __repr__
    print(first) # uses __str__



    # Table 6-1. Magic methods for comparison
    # __eq__( self, other ) self == other
    # __ne__( self, other ) self != other
    # __lt__( self, other ) self < other
    # __gt__( self, other ) self > other
    # __le__( self, other ) self <= other
    # __ge__( self, other ) self >= other
    #
    # Table 6-2. Magic methods for math
    # __add__( self, other )self + other
    # __sub__( self, other )self - other
    # __mul__( self, other )self * other
    # __floordiv__( self, other ) self // other
    # __truediv__( self, other )self / other
    # __mod__( self, other )self % other
    # __pow__( self, other )self ** other
    #
    # Table 6-3. Other, miscellaneous magic methods
    # __str__( self )
    # str( self )
    # __repr__( self ) repr( self )
    # __len__( self )
    # len( self )






    print('End')


# Construct to not include whole program in other includes
if __name__ == "__main__":
    main()