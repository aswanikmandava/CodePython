# Application of decorators is bottom up
# The decorator at the bottom will be executed first and then the one above

"""
When stacking decorators, it's a common practice to use functools.wraps to ensure that the 
metadata of the original function is preserved throughout the stacking process. 
This helps maintain clarity and consistency in debugging and understanding the properties of 
the decorated function.
"""
import functools

def make_me_uppercase(func):
    def wrapper(name):
        greeting = func(name)
        return greeting.upper()
    return wrapper


def add_exclamation(func):
    @functools.wraps(func)
    def wrapper(name):
        greeting = func(name)
        return f"{greeting} !!!"
    return wrapper

@add_exclamation
@make_me_uppercase
def greet(name):
    return f"Hello, {name}"


# multi_decorated_fn = add_exclamation(make_me_uppercase(greet))
# print(multi_decorated_fn("Aswani"))

print(greet("Aswani"))