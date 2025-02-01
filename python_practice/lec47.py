#Classes and files
from time import sleep


class Player():
    def __init__(self, person, word):
        self.person = person
        self.word = word

    def says(self):
        return self.word

class Batsman(Player):
    def says(self):
        return print(self.word + ' batsman')

kohli = Batsman("Virat","I'm a")
kohli.says()

#Magic method

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower() #defining meaning of the property, here the "text" is used as the comparsion of the property of both the words(1st word is in the self)

first = Word("Hi")
second = Word("hi")
print(first == second)