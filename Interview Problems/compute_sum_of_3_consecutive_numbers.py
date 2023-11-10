# Find out the highest of 3 consecutive numbers in a given list

from random import randint
mylist = []

# get 10 random integers
for i in range(10):
    mylist.append(randint(1, 50))

biggest = 0
counter = 0
# count of items
item_count = len(mylist)

print(f"Count: {item_count} List: {mylist}")

for item in mylist:
    counter += 1
    print(f"item: {item} counter: {counter}")
    if counter <= 2:
        biggest += item
    else:
        # get the sum of the last 3 items
        print(f"processing {mylist[counter-3:counter]}")
        current_sum = sum(mylist[counter-3:counter])
        print(f"biggest: {biggest} current_sum: {current_sum}")
        if biggest < current_sum:
            biggest = current_sum
            print(f"biggest now: {biggest}")
print(f"biggest: {biggest}")