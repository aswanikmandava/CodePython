"""
Local
Enclosing (nonlocal)
Global
Built-in
"""

testvar = "global variable"

def check():
    global testvar  # with out this we won't be able to change the value
    testvar = "global variable changed"

check()
print(f"Global var check: {testvar}")


def outer():
    testvar = "local variable"  # this is declared in local scope
    def inner():
        nonlocal testvar    # with out this we can't change the value
        testvar = "local variable changed"
    inner()
    print(f"local var check: {testvar}")

outer()