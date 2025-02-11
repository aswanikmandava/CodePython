class Demo:
    def __init__(self):
        self._salary = 0    # protected member
    
    @property               # this decorator enables this method as a getter method
    def salary(self):
        print("inside getter method")
        return self._salary

    @salary.setter          # this decorator enables this method as a setter method
    def salary(self, new_value):
        print("inside setter method")
        self._salary = new_value
    
    @salary.deleter         # this decorator enables this method as a deleter method
    def salary(self):
        print("inside deleter method")
        del self._salary


def main():
    # instantiate Demo object
    d1 = Demo()

    print(d1.salary)    # this calls getter method

    d1.salary = 1000    # this calls setter method

    print(f"After setter method call, salary: {d1.salary}")

    del d1.salary       # this calls deleter method

    # print(f"After deleter method call, salary: {d1.salary}")    # throws AttributeError

main()