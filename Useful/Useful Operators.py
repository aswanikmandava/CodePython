# start from 1 increment by 2 each time; exclude the max value (10)
for i in range(1, 10, 2):
    print(i)

# start from 0 (default) and increment by 1 each time; exclude the max value (5)
for i in range(5):
    print(i)

for index,value in enumerate('helloworld'):
    print(f"{index} -> {value}")

# list of tuples with (index, letter)
print(list(enumerate('hello')))

# create a list of tuples by mapping item to item from lists
letter = ['o', 'n', 'e']
digit = [1, 2, 3]

print(list(zip(letter, digit)))
for item in zip(letter, digit):
    print(item)