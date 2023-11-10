try:
    a = 10/0
    print a
# This is the base class for all built-in non-system-exiting exceptions.
# All user-defined exceptions should also be derived from this class.
except Exception:
    print "General user exception caught !!!"
# This class is the base class for those built-in exceptions that are raised for various arithmetic errors such as :
# OverflowError
# ZeroDivisionError
# FloatingPointError
except ArithmeticError:
    print "Arithmetic exception caught !!!"
