# simple generator for fibonacci series

def fibonacci(limit):
    # init first 2 in the series
    a, b = 0, 1

    while (a < limit):
        yield a
        a, b = b, (a+b)

for item in fibonacci(8):
    print(item)