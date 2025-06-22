# Method Overriding
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self, num1):
        return "{num1} Sound of the Animal"
    
    def speak(self, num1, num2):
        return "Sound of the"
    
class Dog (Animal) :
    def speak(self):
        print(f"The dof makes sound Woof!")

class Cat(Animal):
    def speak(self):
        print(f"Cat makes sound: Meow")

animal = Animal("Krish")
print(animal.speak(1, 3))


