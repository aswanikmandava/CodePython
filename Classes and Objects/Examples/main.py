from Car import Car, Engine, Wheel

c = Car("Honda", "Blue")
print(c.get_details())

eng = Engine()
eng.start()

whl = Wheel()
whl.rotate()