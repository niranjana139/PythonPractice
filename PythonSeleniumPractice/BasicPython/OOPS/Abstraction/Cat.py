from BasicPython.OOPS.Abstraction.Animal import Animal



class Cat(Animal):
    def make_sound(self):
        return "Meow!"
# Usage
cat = Cat()
print(cat.make_sound())  # Output: Meow!