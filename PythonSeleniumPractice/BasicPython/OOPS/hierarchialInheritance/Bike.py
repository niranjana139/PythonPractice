# Child class 2
from BasicPython.OOPS.hierarchialInheritance.Car import Car
from BasicPython.OOPS.hierarchialInheritance.Vehicle import Vehicle


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

# Create objects
car = Car()
bike = Bike()

# Call methods
car.start()  # inherited from Vehicle
car.drive()  # own method

bike.start()  # inherited from Vehicle
bike.ride()   # own method