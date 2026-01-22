class Greet:
    def hello(self, name=None):
        if name:
            print("Hello",name)
            print(f"Hello {name}")
        else:
            print("Hello")

g = Greet()
g.hello()         # Hello
g.hello("Alice")  # Hello Alice
