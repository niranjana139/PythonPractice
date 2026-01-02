from BasicPython.OOPS.multipleinheritance.Father import Father
from BasicPython.OOPS.multipleinheritance.Mother import Mother


# Child class inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        print("Child's skills: Singing, Dancing")
        # Optionally call parent methods
        Father.skills(self)
        Mother.skills(self)

# Create object of Child
c = Child()
c.skills()