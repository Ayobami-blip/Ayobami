tup1 = ('MTH', 'CSC', 'PHY')
print(tup1)

tup2 = ('CVE', ) # add a comma if you are dealing a tuple when one item is present

tup3 = tup1 + tup2 
print(tup3)
# tup1[0] = 'MEE' # you cannot add values to tuple
# print(tup1)

myTuple = tuple(('MTH', 'CSC', 'PHY'))
print(myTuple)

mySet = set()
print(mySet)

integers = {1, 2 ,3, 4}
print(integers)

integers.add(6)
print(integers)

integers.discard(2) # to remove 
print(integers)

integers.remove(3)
print(integers)

# when remove is used with a element that's not present in the set, it'll remove
# discard doesn't

A = {1,2 ,3,4,5}
B = {1,2 ,3,7,8}

union = A | B # for union
print(union)

intersection = A & B
print(intersection)

difference = A - B
print(difference)

symmetric_diff = A ^ B
print(symmetric_diff)

