class StringHandling:

    def __init__(self):
        print("Constructor")

    def string_handling(self ):
        # Original string
        message = "Hello, Python World!"

        # 1. Accessing characters
        print("First character:", message[0])
        print("Last character:", message[-1])

        # 2. Slicing
        print("First 5 characters:", message[:5])
        print("Characters 7 to 12:", message[7:13])

        # 3. String concatenation
        name = "Alice"
        greeting = "Hello, " + name + "!"
        print(greeting)

        # 4. Changing case
        print("Uppercase:", message.upper())
        print("Lowercase:", message.lower())

        # 5. Searching
        print("Does the message contain 'Python'? -", "Python" in message)

        # 6. Replacing
        new_message = message.replace("World", "Universe")
        print("After replace:", new_message)

        # 7. Splitting and joining
        words = message.split()  # splits into list of words
        print("Split into words:", words)
        joined = "-".join(words)
        print("Joined with '-':", joined)

if __name__ == "__main__":
    stringhandle = StringHandling()
    stringhandle.string_handling()

