#Basic Syntax
d1 = {1: 'lion', 2: 'tiger', 3: 'cat'}
print(d1)

#Access using key
print("The value of dictionary with key 1 using get() is ",d1.get(1))
print("The value of dictionary with key 2 using [] is ",d1[1])

# create dictionary using dict() constructor
d2 = dict(a = "parrot", b = "peacock", c = "hen")
print("Dictionary before updating value using [] is ",d2)
d2['a'] = "Great"

print("Dictionary after updating value is ",d2)
d2['d']="cock"
print("Dictionary after updating new value is ",d2)
del d2['d']
print("Dictionary after deleting value using del is ",d2)
d2.pop('a')
print("Dictionary after deleting value using pop is ",d2)
key,value = d2.popitem()
print(f"Dictionary after deleting value using pop item is {key} ,{value}",d2)
d2.clear()
print("Dictionary after clear value is ",d2)
