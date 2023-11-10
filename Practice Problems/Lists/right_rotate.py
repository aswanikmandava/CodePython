# Implement a function right_rotate(lst, k) which will rotate the given list by k. 
# This means that the right-most elements will appear at the left-most position in the list and so on. 
# You only have to rotate the list by one element at a time.

# Rotate by 3 elements
# Input: [10, 20, 30, 40, 50]
# Output: [30, 40, 50, 10, 20]

# time complexity: O(n)
def right_rotate(lst, k):
    num_items = len(lst)
    if (num_items == 0):
        k = 0
    else:
        # The intuition behind taking the modulo is that we would get back the same list 
        # if we were to rotate the list len(lst) times. That’s why we only need to rotate the list 
        # k % len(lst) times and not actually k.
        k = k % (num_items)
    result = list()
    # get the elements from the end
    for i in lst[(num_items)-k:]:
        result.append(i)
    # get the remaining elements
    for i in lst[0:(num_items-k)]:
        result.append(i)
    return result

# Solution-2: Pythonic rotation
def right_rotate(lst, k):
    print("i am here")
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(right_rotate([10, 20, 30, 40, 50], 3))