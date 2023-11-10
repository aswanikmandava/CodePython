"""
Given a list of integers, find all the duplicates that exist in that list.

Input
    A list of duplicate integers
Output
    A list with the duplicates if they exist, and an empty list if they don’t
Sample Input
    lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
Sample Output
    result = [1, 3, 7]
"""

# Solution-1
# Sort the list > traverse each element in the last > compare current one with previous to identify duplicate
# add it to the duplicate list if not already present in it
lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
lst.sort()
dup_list = list()
for i in range(1, len(lst)):
    j = i - 1
    if lst[i] == lst[j] and lst[i] not in dup_list:
            dup_list.append(lst[i])

# Solution-2
"""
While traversing, the element is made the key of the dictionary and its value is set to 1. 
If the element occurs again in the list, the value corresponding to the dictionary key (which has that element) is 
updated and the element is put in the list. This continues until the list is fully traversed. 
In the end, the list is returned with all the elements that have duplicate entries
"""
# dict to keep track of element and its occurrences
item_tracker = dict()

# list to add duplicate elements
dup_list = list()

for ele in lst:
    if ele not in item_tracker: # add to dict
        item_tracker[ele] = 1
    else:
        if item_tracker[ele] == 1:
            dup_list.append(ele)
        item_tracker[ele] += 1

print(item_tracker)
print(dup_list)