# Abstract BAse Class (ABC) are used to define common methods for a group of related objects.
# They can enforce the drive classes implement particular methods.

from abc import ABC, abstractmethod
# Define Abstract Base Class
class Vehicle(ABC):

    def driv(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"Car Enginer Has Started")



class Bike(Vehicle):
    def start_engine(self):
        print(f"Bike engine has started")

    def show_data(self):
        print(f"Bike engine has started")

def start_vehicle_engine(vehicle):
    vehicle.start_engine()

car = Car()
bike = Bike()
bike.start_engine()
bike.show_data()
start_vehicle_engine(car)
start_vehicle_engine(bike)
