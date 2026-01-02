# List is an iterable
numbers = [1, 2, 3]

# Get an iterator from the list
iterator = iter(numbers)

# Use next() to get elements one by one
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  #  Raises StopIteration .
'''StopIteration is a built-in exception that is raised
 automatically by an iterator to signal that there are no more items to return.'''
