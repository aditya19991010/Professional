#  . a. Create a class called Animal() - Define 3 instance variables - phylum,
# _limbs, _voice. Initialize variables _limbs to 4 and _voice to “A generic Animal
# Sound” in class . In the __init__(self, phylum) method, set the phylum instance
# variable to the passed value

class Animal:
    phylum =""
    _limbs=4
    _voice = "A generic Animal Sound"

    def __init__(self, phylum):
        self.phylum = phylum

    @staticmethod
    def kingdom():
        return print("Animalia")

    def getPhylum(self):
        return print(self.phylum)

    @property
    def legs(self):
        return print(self._limbs)

    @legs.setter
    def legs(self,value):
        self._limbs = value

    @property
    def sound(self):
        return print(self._voice)

    @sound.setter
    def sound(self,value):
        self._voice = value

    @classmethod
    def getDescription(cls):
        return cls.__name__

human = Animal("Mammalia")
dog = Animal("Mammalia")
pigeon = Animal("Aves")

dog.legs
pigeon.legs
human.sound