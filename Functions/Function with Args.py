# function arguments are passed by reference
# Any changes made to the argument inside the function is also visible in the calling function

# Required arguments
def change_list(mylist):
    print("inside function")
    mylist.append(5)
    print("List:", mylist)
    print("exiting function")
    return


numbers = [1, 2, 3, 4]
change_list(numbers)
print("List:", numbers)

# keyword arguments
# order doesn't matter in this case if you use same argument names
def print_args(name, age):
    print("Name:", name)
    print("Age:", age)
    return


print_args(age=34, name="Aswani")

# arguments with default values
# if values not passed to function then default values will be set
def print_args2(name="Aswani", age=30):
    print("Name:", name)
    print("Age:", age)
    return


print_args2(name="Mandava", age=33)
print_args2()
print_args2(name="Kumar")
print_args2(age=29)


# function with variable number of arguments
def print_vars(*vartuple):
    print("processing variable number of arguments")
    for arg in vartuple:
        print("arg:", arg)
    return

def func(*myarg):
    myList = []
    for arg in myarg:
        myList.append(arg)
    return len(myList)

# function with variable number of keyword arguments
def print_kvars(**params):
    for key,value in params.items():
        print(f"{key} -> {value}")

print_kvars(name='Aswani', num=10, male=True)
num = [1, 2, 3, 4]
print('Length:', func(1,2,3,4))

print_vars("Aswani", 34, 174)
print_vars(3.413, False)

# function with return value
def sum(var1=0, var2=0):
    return var1 + var2


total = sum(100, 11)
print("Total:", total)
total = sum(50)
print("Total:", total)
