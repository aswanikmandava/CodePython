try:
    print "Raising exception"
    raise NameError("Hello")
except NameError:
    print "Exception caught !!!"
