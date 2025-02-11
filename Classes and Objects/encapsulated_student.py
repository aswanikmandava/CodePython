# Example class that implements rules of encapsulation

class Student:
    def __init__(self, name, rollNumber):
        # private properties
        self.__name = name
        self.__rollNumber = rollNumber
    
    # public methods to get/set private properties
    def getName(self):
        return self.__name

    def setName(self, new_name):
        self.__name = new_name

    def getRollNumber(self):
        return self.__rollNumber
  
    def setRollNumber(self, new_number):
        self.__rollNumber = new_number
  
# create student objects
s1 = Student('Aswani', 100)
print(s1.getName())
# change name
s1.setName('Aswani Kumar')
print("Name after modification: ", s1.getName())
  
print(s1.getRollNumber())
# modify roll no
s1.setRollNumber(200)
print("Roll No after modification: ", s1.getRollNumber())
