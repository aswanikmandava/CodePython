# # define class and its methods
# class Robot:
#     def introduce_self(self):
#         print("My name is %s" % self.name)
#
# # create object
# r1 = Robot()
#
# # set properties
# r1.name = "Tom"
# r1.weight = 30
# r1.color = "red"
#
# # call method
# r1.introduce_self()

# Better way to set object properties to use constructor method
# every method must have self as the first parameter
class Robot:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def introduce_self(self):
        print("My name is {}".format(self.name))


# create objects
r1 = Robot('Rob', 30, 'red')
r2 = Robot('Tom', 40, 'green')

print(type(r1))
# call method on the object
r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person('Aswani', 'Calm', True)
p1.stand_up()
print("{} is_sitting: {}".format(p1.name, p1.is_sitting))

p1.owns_robot = r2
p1.owns_robot.introduce_self()

p2 = Person('Suneetha', 'Aggressive', False)
p2.sit_down()
print("{} is_sitting: {}".format(p2.name, p2.is_sitting))
p2.owns_robot = r1
p2.owns_robot.introduce_self()
