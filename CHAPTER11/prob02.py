#create class'pets'fromclass 'animal' and further create a class dogs from pets . add a method bark to class dog
class Animal:
    pass

class Pet(Animal):
    pass

class Dog(Pet):
    def bark(self):
        print("woof woof")

d = Dog()
d.bark()