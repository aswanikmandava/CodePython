"""
Shape is the base class with an __init__ method to initialize the color attribute and an abstract area method. 
Circle is a subclass of Shape that extends it by adding a radius attribute. 
It calls the superclass constructor using super() to initialize the common attribute. 
The area method is overridden in the Circle subclass to provide a specific implementation for calculating the area of a circle.
"""
class Shape:
    def __init__(self, color):
        # Storing the color of the shape
        self.color = color

    def area(self):
        # This method should be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, color, radius):
        # Initialize the parent class (Shape) with color
        super().__init__(color) 
        # Storing the radius of the circle
        self.radius = radius  

    def area(self):
        # Circle-specific area calculation
        return 3.14 * self.radius ** 2

# Creating instances
# Shape instance with color 'Red'
s = Shape("Red")  

# Circle instance with color 'Blue' and radius 5
c = Circle("Blue", 5)

# Accessing attributes and methods
print(s.color)  # Output: Red
print(c.color)  # Output: Blue
print(c.radius)  # Output: 5
print(c.area())  # Output: 78.5
