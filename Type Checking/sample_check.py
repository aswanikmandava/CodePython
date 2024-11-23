def greet_me(name: str) -> str:
    return f"Hello, {name} !!!"

# annotates myname variable to be a string
myname: str = "Aswani"

# display annotations of function
print(greet_me.__annotations__)

print(greet_me(myname))