class Student:
    # Class variable (shared by all objects)
    school_name = "ABC High School"

    def __init__(self, name, grade):
        # Instance variables (unique to each object)
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")


# Create two student objects
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Accessing class and instance variables
student1.display()
student2.display()

# Changing instance variable (only for student1)
student1.grade = "A+"

# Changing class variable (affects all instances)
Student.school_name = "XYZ International School"

print("\nAfter updating:")
student1.display()
student2.display()
