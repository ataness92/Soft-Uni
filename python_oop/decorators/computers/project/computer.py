from abc import ABC, abstractclassmethod

class Computer(ABC):

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    
    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self,value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty")

        self.__model = value

    def configure_computer(self, processor: str, ram: int) -> str:
        #TODO: finish this
        pass

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} " \
               f"and {self.ram}GB RAM"

               
