myList = [1, 2, 3]
try:
    print "Item-2: %d" %(myList[1])
    # Throws error since there are only 3 items
    print "Item-4: %d" %(myList[3])
except IndexError:
    print "An error occurred accessing an non-existing item"
