# Concrete subclass
from BasicPython.OOPS.Abstraction.Animal import Animal


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Usage
dog = Dog()
print(dog.make_sound())  # Output: Woof!

