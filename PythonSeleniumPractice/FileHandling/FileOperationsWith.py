# 1. Write contacts to a file (create or overwrite)
with open("contacts.txt", "w") as file:
    file.write("Name: Alice, Phone: 1234567890\n")
    file.write("Name: Bob, Phone: 9876543210\n")

# 2. Append a new contact to the file
with open("contacts.txt", "a") as file:
    file.write("Name: Charlie, Phone: 5551234567\n")

# 3. Read and print all contacts from the file
with open("contacts.txt", "r") as file:
    print("📇 Contact List:")
    for line in file:
        print(line.strip())

#with automatically handles close() . So, close() is not used
