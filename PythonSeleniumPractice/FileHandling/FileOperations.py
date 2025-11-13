# 1. Write to a file (creates or overwrites)
file = open("contacts.txt", "w")
file.write("Name: Alice, Phone: 1234567890\n")
file.write("Name: Bob, Phone: 9876543210\n")
file.close()  # Important: close the file!

# 2. Append a new contact
file = open("contacts.txt", "a")
file.write("Name: Charlie, Phone: 5551234567\n")
file.close()

# 3. Read and display contacts
file = open("contacts.txt", "r")
print("📇 Contact List:")
for line in file:
    print(line.strip())
file.close()
