"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

# multiply argument a with argument b and return result

myfunc = lambda a, b: a*b
print(myfunc)
result = myfunc(2, 10)
print(f"result: {result}")