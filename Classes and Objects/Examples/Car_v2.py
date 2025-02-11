class Engine:
    def start(self):
        print("Engine started")

class Wheel:
    def rotate(self):
        print("wheel rotated")

class Carv2:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
    
    def get_details(self):
        return f"{self.color} {self.model}"
    
    def start(self):
        self.engine.start()

    def drive(self):
        for obj in self.wheels:
            obj.rotate()

    def __repr__(self):
        return f"Color: {self.color} | Model: {self.model}"


def main():
    c1 = Carv2("Honda", "Gray")
    c1.get_details()
    c1.start()
    c1.drive()

main()