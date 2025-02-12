# ways to initialize a list

def myfunc():
    print("hello func !!!")


mylist_1 = list()
mylist_2 = [1, 10, 200]
mylist_3 = list(range(10))
mylist_4 = ['a', 2.0, 30, myfunc]

# since list is heterogenous, it can include different data types including functions as well

# invoking a function in a list
mylist_4[3]()