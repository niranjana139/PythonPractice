# Define a class
class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance of Student)
student1 = Student("Alice", 20)

# Access object attributes and methods
print("Name:", student1.name)
print("Age:", student1.age)

student1.greet()  # Call method
