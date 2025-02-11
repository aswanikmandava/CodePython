class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def get_details(self):
        return f"{self.color} {self.model}"

    def __repr__(self):
        return f"Color: {self.color} | Model: {self.model}"

class Engine:
    def start(self):
        print("Engine started")

class Wheel:
    def rotate(self):
        print("wheel rotated")