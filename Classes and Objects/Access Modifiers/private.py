"""
The members of a class that are declared private are accessible within the class only, private access modifier is the most 
secure access modifier. Data members of a class are declared private by adding a double underscore '_' symbol before the 
data member of that class. 
"""
class Student:
    # private members
    __name = None
    __branch = None
    def __init__(self, name, branch) -> None:
        self.__name = name
        self.__branch =  branch
    # private member function
    def __get_details(self):
        print(f"name: {self.__name}")
        print(f"branch: {self.__branch}")
    
    # public member function
    def get_details(self):
        print(f"name: {self.__name}")
        print(f"branch: {self.__branch}")

# attempt to access private members or member function will throw error
    # AttributeError: 'Student' object has no attribute '__get_details'
s = Student(name='Aswani', branch='CSIT')
# s.__get_details()
# print(s.__name)
s.get_details()