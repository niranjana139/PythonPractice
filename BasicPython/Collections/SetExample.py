#Basic syntax
s = {10,40,20}
print(s,type(s))

#Type casting from list or tuple
s1=set([1,2,4])
print(s1,type(s1))

tup = (1,2,3,4)
list1 =[3,4,5]
s.add(tup)
print("Adding tuple", tup,"to the set ", s ," using add method is ",s)
s.update(list1)
print("Adding List ",list1 , "to set ",s ," using update method is ",s)

s.clear()
print("Clearing set using clear method is ",s)


#difference doesn't overwrite the lefthand side while difference_update overwrites left hand side
a = {1,2,3,4,5}
b= {2,5,4,3,1,8,9,10}
print(a,type(a))
#print("Difference between ",a," and ",b," is ",a.difference(b))

print("post", a)
a.difference_update(b)
print("a is " ,a)
print("b is ", b)
#Checks for subset and returns True or False
print("checking if ",a," is subset of ",b,"is ",a.issubset(b))
#Checks for superset and returns True or False
print("checking if ",b," is superset of ",a," is ",b.issuperset(a))

#isDisJoint() returns true if no common elements are there
print("Checking if ",a," is disjoint of ",b," is ",a.isdisjoint(b))

#Removes 5 from set a if there. else, value error is thrown
a.remove(5)

#Sorts in ascending order. Reverse order is not possible in sets
print("Sorted set of ",b," is ",sorted(b))

#A frozen set
x = frozenset([1,2,4])
print(x,type(x))
