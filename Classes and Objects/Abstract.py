class Animal():
    def __init__(self, name):
        self.name = name
        print("Animal instantiated")

    def get_sound(self):
        raise NotImplementedError("Subclass must implement this method !!!")
    
    def get_name(self):
        return self.name


class Dog(Animal):
    def get_sound(self):
        return "{} says bow bow !!!".format(self.name)

try:
    myanimal = Animal('Dog')
    print(f"Name of animal: {myanimal.get_name()}")
    myanimal.get_sound()
except Exception as e:
    print("Caught exception: {}".format(e))

mydog = Dog('tommy')
print(mydog.get_sound())
