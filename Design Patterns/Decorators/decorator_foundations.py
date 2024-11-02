# A decorator is a design pattern in Python that allows a user to add new functionality to an 
# existing object without modifying its structure. Decorators are typically applied to functions, 
# and they play a crucial role in enhancing or modifying the behavior of functions

# To define a general purpose decorator that can be applied to any function we use 
# args and **kwargs. args and **kwargs collect all positional and keyword arguments and 
# stores them in the args and kwargs variables. args and kwargs allow us to pass as many 
# arguments as we would like during function calls.

# embedded function (function definition inside a function)
def greet(name):
    def add_greeting(name):
        return f"Hello, {name}"
    res_greeting = add_greeting(name)
    return res_greeting
print("Function inside a function example")
print(greet("Aswani"))

# passing function as a argument
def num_add(num):
    return num + 1

def increment(func):
    # takes another function as an arg
    num_to_add = 3
    return func(num_to_add)

print("Passing function as an argument example")
print(increment(num_add))

# function returning another function
def fn_greet():
    def add_greeting(name):
        return f"Hello, {name}"
    return add_greeting

greet_me = fn_greet()
print(greet_me("Aswani"))