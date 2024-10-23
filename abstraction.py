# method of abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop (self):
        pass

class Vehicle(Car):
    def start(self):
        return "Car engine has started"
    def stop(self):
        return "Car engine has stopped"

def operate_vehicle(vehicle:Vehicle):
    print(vehicle.start())
    print(vehicle.stop())

car = Vehicle()
operate_vehicle(car)