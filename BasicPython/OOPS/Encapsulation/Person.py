class Person:
    def __init__(self, name, age):
        self.name = name            # Public
        self._age = age             # Protected
        self.__ssn = "123-45-6789"  # Private

    # Getter for private variable
    def get_ssn(self):
        return self.__ssn

    # Setter for private variable
    def set_ssn(self, new_ssn):
        self.__ssn = new_ssn

# Create object
p = Person("Alice", 30)

print(p.name)        # ✅ Public: accessible
print(p._age)        # ⚠️ Protected: accessible, but not recommended
# print(p.__ssn)     # ❌ Private: raises AttributeError

print(p.get_ssn())   # ✅ Accessing private variable via getter
