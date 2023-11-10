class Person:
    def __init__(self, name, age) -> None:
        # public data members
        self.name = name
        self.age = age
    # public member function
    def getName(self):
        # accessing public data member
        return self.name


# create obj
p = Person(name='Aswani', age=39)

print(f"attribute access: {p.age}")
print(f"method access: {p.getName()}")