myList = ['x','b','c','x','d']

#Adds a value in specified index
myList.insert(2,'y')
print(myList)

#Appends the value 'e' to the list
myList.append('e')
print(myList)

#Finds the index of provided value. If no such value is there, value error is returned
print(myList.index('d'))

#Removes element in specified index from the list. If no value is specified, last element of list is removed
myList.pop(2)

#Copies the whole list to a new one
myCopyList = myList.copy()

#Sorts the list in ascending order
myList.sort()
print(myList)
myList[1]="m"
print(myList)
#reverse=True returns the sorted list in descending order
myCopyList.sort(reverse=True)

#Reverses the list
print(myList)
myList.reverse()
print("reversed list is ",myList)
#Returns the number of occurences of given value is returned. If no such value is found, then zero is returned
print(myList.count('x'))

#Removes the first occurence of  value specified in list
myList.remove('x')

print(myList)
