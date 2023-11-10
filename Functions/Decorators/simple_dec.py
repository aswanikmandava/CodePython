"""
decorator is an efficient way to add extra functionality to an existing function
enable it by adding @ line at the top of the function
disable the decorator by removing the @ line
"""
def hello(name='Unknown'):
    def greet():
        return f"\t Hello {name}, welcome to the decorator world !!!"
    def welcome():
        return "\t welcome !!!"
    # print("returning a function conditionally ...")
    if name != 'Unknown':
        return greet
    return welcome

# newfunc = hello()
newfunc = hello('Aswani')   # returns a function
# print(newfunc())    # execute the returned function

def feature(subfeature):    # takes a function as an argument
    print("existing feature code")
    print(subfeature())    # executes the passed function

def new_decorator(original_func):
    def wrap_func():
        print("original function code")
        original_func()
        print("extra code")
    return wrap_func

# def func_needs_decorator():
#     print("I want to be decorated")

# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

# lines 31-34 can be re-written as
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()
