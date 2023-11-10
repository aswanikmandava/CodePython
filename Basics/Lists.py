# when to use lists or arrays
"""
Because of the way that lists are implemented, elements can be appended to them very efficiently. 
If you want your collection to grow and shrink in a time-efficient manner, then lists should be used. 
It’s also better to use lists if you need to manage lots of different data types, however, arrays are better when 
you need to store a lot of data and perform a large number of computationally intensive mathematical operations. 
Note that the arrays from the NumPy library of Python are better suited for mathematical use cases.
"""
myList = [1, 2, 4, 'hello']
second_list = ['a', 'b', 'c']

# copy a list
another_list = myList.copy()

# add an element to the end of a list
# O(1)
myList.append(10)
print(myList)

# add an element before the index
# O(n)
myList.insert(0, 15)
# print second item in the list
print(myList[1])

# remove last item in the list
# O(1)
myList.pop()
print(myList)

# remove 3rd item in the list or element at index 2
# O(k) where k < n
myList.pop(2)
del myList[2]
print(myList)

print(f"myList before: {myList}")
# remove element in list by value
# O(n)
myList.remove(2)
print(myList)
print(f"myList after: {myList}")

# reverse a list
# O(n)
myList.reverse()

# Add a list to the current list
myList.extend(second_list)
print(myList)