# Given two sorted lists, merge them into one list which should also be sorted.

# in place merge
# time complexity: O(m(n+m))
def merge_lists(lst1, lst2):
    ind1 = 0  # Creating 2 new variables to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1

# using a separate list
# time complexity: O(n+m)
def merge_lists(lst1, lst2):
    ind1 = 0
    ind2 = 0
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    res = list() # result list
    res_ind = 0 # index to the result list
    # fill up the required size for result list to avoid index error
    for i in range(lst1_len + lst2_len):
        res.append(i)
    while (ind1 < lst1_len and ind2 < lst2_len):
        if lst1[ind1] < lst2[ind2]:
            res[res_ind] = lst1[ind1]
            ind1 += 1
            res_ind += 1
        else:
            res[res_ind] = lst2[ind2]
            ind2 += 1
            res_ind += 1
    while (ind1 < lst1_len):
        res[res_ind] = lst1[ind1]
        ind1 += 1
        res_ind += 1
    while (ind2 < lst2_len):
        res[res_ind] = lst2[ind2]
        ind2 += 1
        res_ind += 1
    return res


print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))