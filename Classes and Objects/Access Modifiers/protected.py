"""
The members of a class that are declared protected are only accessible to a class derived from it. 
Data members of a class are declared protected by adding a single underscore "_" symbol before the data member of that class.
"""

class Student:
    # protected data members
    _name = None
    _branch = None

    def __init__(self, name, branch) -> None:
        self._name = name
        self._branch = branch
    
    # protected member function
    def _display_details(self):
        # accessing protected data members
        print(f"name: {self._name}")
        print(f"name: {self._branch}")


# derived class
class RegularStudent(Student):
    def __init__(self, name, branch) -> None:
        Student.__init__(self, name, branch)
    
    # public member function
    def get_details(self):
        # accessing protected member function of super class
        self._display_details()

s = RegularStudent(name='Aswani', branch='CSIT')
s.get_details()

# doesn't prevent from accessing protected ones outside the class but refrain from doing it
s2 = Student(name='Aswani', branch='CSIT')
s2._display_details()