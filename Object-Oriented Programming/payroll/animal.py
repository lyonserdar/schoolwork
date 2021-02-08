# animal.py: Illustrates calling superclass constructors

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        print("Animal.__init__")
        self.name = name

    def whoAmI(self):
        return self.name


class SpeakingAnimal(Animal):
    @abstractmethod
    def speak(self):
        pass


class Dog(SpeakingAnimal):
    def speak(self):
        return "Bark!"


class Antelope(Animal):
    pass


d = Dog("Muffy")
a = Antelope("Annie")

animals = [d, a]
for animal in animals:
    print(animal.whoAmI(), end="")
    speech = ": " + animal.speak() if isinstance(animal, SpeakingAnimal) else ""
    print(speech)
print(isinstance(d, SpeakingAnimal))