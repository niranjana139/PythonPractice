# Parent class 1 (inherits from Vehicle) - multilevel part
from BasicPython.OOPS.hybridinheritance.Vehicle import Vehicle


class Car(Vehicle):
    def drive(self):
        print("Car is driving")
