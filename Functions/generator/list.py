mylist = [1, 10, 20, 50, 100]

# convert list object into an iterator
my_iterator = iter(mylist)

while True:
    try:
        print(next(my_iterator))
    except Exception as e:
        print(f"ERR: {e}")
        break