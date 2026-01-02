# Using String
myTup1 = ('Geeks', 'For')
print("Tuple using String is ", myTup1)
#Access tuple using index value
print("First value of tuple is ",myTup1[0])

# Using List
myList = [1, 2, 4, 5, 6]
myTup2 = tuple(myList)

#Tuple can be unpacked to variables, provided, number of variables to unpack is same as the size of tuple
a,b,c,d,e = myTup2
print(f"Unpacked tuple is {a},{b},{c},{d},{e}")
print("Conversion of list to tuple is ",myTup2)

#Access a range of elements using slicing
print("Accessed using slicing with index 1-3 and till 1 are ",myTup2[1:4],"and ",myTup2[:2])


myList = [1, 2, 4, 5, 6]
myTup2 = tuple(myList)

#Concatenate the tuples using + sign
myConcatTup = myTup1 + myTup2
print(f"Concatenated tuple of {myTup1} and {myTup2} are {myConcatTup}")


# Define a tuple
numbers = (10, 20, 30, 40, 50, 60, 70)

print("Original tuple:", numbers)

# Slice from index 1 to 4 (20, 30, 40)
print("numbers[1:4]:", numbers[1:4])

# Slice from beginning to index 3 (10, 20, 30)
print("numbers[:3]:", numbers[:3])

# Slice from index 3 to end (40, 50, 60, 70)
print("numbers[3:]:", numbers[3:])

# Slice with step of 2 (every second element)
print("numbers[::2]:", numbers[::2])

# Reverse the tuple
print("Reversed tuple:", numbers[::-1])

# Create a tuple
my_tuple = (10, 20, 30)

# Delete the tuple
del my_tuple

# Try to access it (will cause an error)
# print(my_tuple)  # NameError: name 'my_tuple' is not defined
