class Animal():
    def __init__(self, legs=4):
        self.legs = legs
        print("Animal instantiated")
    def get_type(self):
        if self.legs == 0:
            return "Reptile"
        elif self.legs == 4:
            return "Mammal"
        else:
            return "Unknown"
    def get_sound(self):
        return "Woof !!!"

# create another class that inherits Animal
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog instantiated")
    # overriding get_sound
    def get_sound(self):
        return "Bow Bow !!!"

mydog = Dog()
print("Type: {}".format(mydog.get_type()))
print("Sound: {}".format(mydog.get_sound()))
