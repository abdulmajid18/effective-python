from abc import ABC, abstractmethod


# Abstract class (Product)
class Car(ABC):
    @abstractmethod
    def create(self):
        pass


# Concrete Product 1
class Sedan(Car):
    def create(self):
        return "Sedan Car Created"


# Concrete Product 2
class SUV(Car):
    def create(self):
        return "SUV Car Created"


# Concrete Product 3
class Truck(Car):
    def create(self):
        return "Truck Car Created"


# Factory Class
class CarFactory:
    @staticmethod
    def get_car(car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        elif car_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown car type")


# Client Code
car_type = input("Enter car type (sedan/suv/truck): ").strip().lower()
car = CarFactory.get_car(car_type)
print(car.create())
