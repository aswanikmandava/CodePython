"""
A closure is an inner/nested function that keeps the data regarding its enclosing scope
even after the closure is called
"""

import math

def multiply():
    mylist = []
    def closure(num):
        mylist.append(num)
        return math.prod(mylist)
    return closure

multiply_v2 = multiply()
print(multiply_v2(2))
print(multiply_v2(3))
print(multiply_v2(4))