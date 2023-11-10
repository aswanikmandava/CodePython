# Handle multiple exceptions
try:
    a = 6
    if a <= 3:
        b = a/(a-3)
    # throws NameError when a > 3
    print "Value of b: %d" %b
except (ZeroDivisionError, NameError):
    print "An error occurred"
else:
    print "No exception raised"

