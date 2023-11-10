"""
A Generator in Python is a function that returns an iterator using the Yield keyword
A generator function in Python is defined like a normal function, but whenever it needs to generate a value, 
it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically 
becomes a Python generator function. 
"""

def get_an_iterator():
    yield 1
    yield 2
    yield 3


for item in get_an_iterator():
    print(item)

# Iterating over the generator object using next
 
# In Python 3, __next__()
print(next(get_an_iterator()))