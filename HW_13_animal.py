from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("woof-woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class AnimalFactory:
    @staticmethod
    def create_animal(name):
        if name == "dog":
            return Dog()

        elif name == "cat":
            return Cat()

        else:
            raise TypeError

animal = AnimalFactory.create_animal("cat")
animal.speak()
