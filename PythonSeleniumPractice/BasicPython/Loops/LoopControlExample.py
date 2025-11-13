print("Example of break:")
for i in range(1, 6):
    if i == 3:
        print("Break at i =", i)
        break  # Exit loop when i == 3
    print(i)

print("\nExample of continue:")
for i in range(1, 6):
    if i == 3:
        print("Continue at i =", i)
        continue  # Skip the rest of the loop when i == 3
    print(i)

print("\nExample of pass:")
for i in range(1, 4):
    if i == 2:
        pass  # Does nothing, placeholder
        print("Pass at i =", i)
    else:
        print(i)
