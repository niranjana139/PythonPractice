# Derived class (Child)
from BasicPython.OOPS.multilevelinheritance.Dog import Dog


class Puppy(Dog):
    def weep(self):
        print("Puppy weeps.")

# Create object of the lowest-level class
p = Puppy()

# Access methods from all levels
p.sound()   # From Animal
p.bark()    # From Dog
p.weep()    # From Puppy