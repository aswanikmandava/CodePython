class Circle():
    # Class attribute
    pi = 3.14

    # Constructor method
    def __init__(self, radius = 1):
        self.radius = radius

    # Methods
    def get_circumference(self):
        return 2*self.radius*Circle.pi

    def get_area(self):
        return self.radius*self.radius*Circle.pi

# end of class

cir = Circle(2)
print("rd: {}".format(cir.radius))
print("circumference: {}".format(cir.get_circumference()))
print("area: {}".format(cir.get_area()))