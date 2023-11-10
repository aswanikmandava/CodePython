# arrays in python contains elements of same datatype

"""
Python lists are very flexible and can hold completely heterogeneous arbitrary data, 
but they use a lot more space than Python arrays. Each list contains pointers to a block of pointers, 
each of which in turn points to a full Python object. Again, the advantage of the list is flexibility: 
because each list element is a full structure containing both data and type information, the list can be filled 
with data of any desired type. Arrays lack this flexibility but are much more efficient for storing and manipulating data.
"""

import array

num = [10, 20, 30]
chars = ['a', 'b', 'c']

# type code
# i - integer
# u - unicode char
# f - float
# a = array.array('i', num)
c = array.array('u', chars)

# iterate through the elements
for item in c:
    print(item)

# insert an element before an index
chars.insert(len(chars)-1, 'd')
print(chars)

# delete an element
del chars[3]
print(chars)

print(f"before replacement: {chars}")
# replace a range of chars (2-4)
chars[2:5] = array.array('u', ['x', 'y', 'z'])
print(chars)