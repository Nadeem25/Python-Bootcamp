class Car:
    def __init__(self, windows, door):
        self.windows = windows
        self.door = door

    def drive(self):
        print(f"Person is driving the car which has {self.windows} windows and {self.door} door")

class Tesla(Car):
    def __init__(self, windows, door, is_self_drive):
        super().__init__(windows, door)
        self.is_self_drive = is_self_drive

    def selfDriving(self):
        print(f"Tesla Supports Self Driving: {self.is_self_drive}")

tesla_obj = Tesla(4, 4, True)
tesla_obj.selfDriving()
tesla_obj.drive()

# Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog (Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(name)
        Pet.__init__(owner)