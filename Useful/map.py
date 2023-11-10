import pprint
# built-in map can be used to transform one iterable to another iterable using an expression
# example: to remove leading/trailing white spaces in a list of words
words = [' hello', 'world  ', ' how ']
t_words = list(map(str.strip, words))
print(t_words)

# to return the square of each item in a list
num = [1, 2, 3, 4]
num2 = list(map(lambda i: i**2, num))
print(f"square result: {num2}")

# to return an item from one list to the power of an item in same position from an another list
# if mismatch in the number among the 2 lists, processing stops at the end of shortest list
l1 = [2, 5, 6, 7, 8]
l2 = [1, 3, 5, 7]
l3 = list(map(pow, l1, l2))
print(l3)