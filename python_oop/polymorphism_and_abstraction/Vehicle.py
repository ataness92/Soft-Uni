from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle):
    CONDITIONER_ON: float = 0.9

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption+self.CONDITIONER_ON)*distance:
            self.fuel_quantity -= (self.fuel_consumption+self.CONDITIONER_ON)*distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON: float = 1.6
    TANK_PERCENTAGE_FILL: float = 0.95

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + self.CONDITIONER_ON)*distance:
            self.fuel_quantity -= (self.fuel_consumption + self.CONDITIONER_ON)*distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel*self.TANK_PERCENTAGE_FILL

