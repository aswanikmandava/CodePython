# Arrange elements in such a way that the maximum element appears at first position, 
# then minimum at second, then second maximum at third and second minimum at fourth and so on.
# 
# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list 
# such that the 0th index will have the largest number, the 1st index will have the smallest, 
# and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices 
# will have the largest numbers in the list in descending order and the odd-numbered indices will have 
# the smallest numbers in ascending order.

def linear_sort(lst):
    print(f"input: {lst}")
    count = len(lst)
    if count <=1 :
        return lst
    for i in range(1, count):
        key = lst[i]
        j = i - 1
        while (j >= 0 and key < lst[j]):
            # print(f"j={j}, {key} < {lst[j]}, changing {lst[j+1]} with {lst[j]}")
            lst[j+1] = lst[j]
            j -= 1
        # print(f"assigning {lst[i]} with {key}")
        lst[j+1] = key




def max_min(lst):
    count = len(lst)
    linear_sort(lst)
    print(f"sorted list: {lst}")
    # reverse the list using slicing
    desc_lst = lst[::-1]
    result = list()
    for i in range(count):
        if i % 2 == 0:
            result.append(desc_lst.pop(0))
        else:
            result.append(lst.pop(0))
    return result
    

print(max_min([1, -2, 3, 40, 5, 0, 7]))
