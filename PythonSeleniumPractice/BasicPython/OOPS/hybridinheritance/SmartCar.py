# Child class inherits from both Car and MusicSystem - multiple inheritance part
from BasicPython.OOPS.hybridinheritance.Car import Car
from BasicPython.OOPS.hybridinheritance.MusicSystem import MusicSystem


class SmartCar(Car, MusicSystem):
    def auto_pilot(self):
        print("Auto pilot enabled")

# Create an object of SmartCar
sc = SmartCar()

# Access methods from all parent classes
sc.start()        # from Vehicle
sc.drive()        # from Car
sc.play_music()   # from MusicSystem
sc.auto_pilot()   # from SmartCar itself