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

class WildAnimal():
    def __init__(self, name) -> None:
        self.name = name
    
    def attack(self):
        return f"{self.name} can attack"

class DomesticAnimal():
    def __init__(self, name) -> None:
        self.name = name
    
    def milk(self):
        return f"{self.name} can give milk"

# create another class that inherits Animal and DomesticAnimal
class Goat(Animal, DomesticAnimal):
    def __init__(self, name):
        Animal.__init__(self)
        DomesticAnimal.__init__(self, name)
        print("Goat instantiated")


mygoat = Goat(name='abc')
print(f"{mygoat.name} has {mygoat.legs} legs")
print("Type: {}".format(mygoat.get_type()))
print("Milk: {}".format(mygoat.milk()))
