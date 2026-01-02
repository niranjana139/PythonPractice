from BasicPython.OOPS.singleInheritance.Animal import Animal


# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} b                                                   arks.")

# Create an object of Dog
d = Dog("Buddy")

# Call methods from both parent and child
d.speak()  # inherited from Animal
d.bark()   # defined in Dog
