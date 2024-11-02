def make_me_uppercase(func):
    def wrapper(name):
        greeting = func(name)
        return greeting.upper()
    return wrapper

@make_me_uppercase
def greet(name):
    return f"Hello, {name}"


# decorated_fn = make_me_uppercase(greet)
# print(decorated_fn("Aswani"))

print(greet("Aswani"))