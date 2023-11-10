#  list[start:end:step]
# list[start:] means all numbers greater than start uptil the range

# list[:end] means all numbers less than end uptil the range

# list[:] means all numbers within the range


mylist = [1, 5, 6, 9, 10]
# first 3 elements 
print(mylist[0:3])
print(mylist[:3])

# second element until last but one
print(mylist[1:len(mylist)-1])
# last 2 elements
print(mylist[len(mylist)-2:len(mylist)])

# all elements of a list
print(mylist[:])

# all elements at even index
print(mylist[::2])

# all elements at odd index
print(mylist[1::2])

# reverse the list using slicing
print(mylist[::-1])
print(mylist)
# delete elements at odd index
del mylist[1:len(mylist):2]
print(mylist)

# slicing string
mystr = "I'm Aswani"
print(mystr[2:])