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
def merge_lists(nums1, nums2):
    """
    Algorithm (Using a separate list with 3 pointers):
        1) Initialize three pointers, p1, p2, and p3, pointing to the start of nums1, nums2, and result, respectively.
        2) Traverse both lists until the end of either nums1 and nums2 is reached.
        3) While traversing, compare the elements of nums1 and nums2, pointed by p1 and p2, respectively. Check whether the element pointed by p1 or p2 is smaller.
        4) If the element pointed by p1 is smaller, store this element at the position pointed by p3. Also, increment p1 and p3 by 1.
        5) Otherwise, if the element pointed by p2 is smaller, store this element at the position pointed by p3. Also, increment p2 and p3 by 1.
        6) After the traversal, append the rest of the elements in any of the lists to result.
    """
    # fill the list with dummies
    result = [None] * (len(nums1)+len(nums2))
    p1 = 0
    p2 = 0
    p3 = 0

    # Traverse both lists until the end of either list is reached
    while (p1 < len(nums1)) and (p2 < len(nums2)):
        # If the value at p1 is smaller than the value at p2, store the value at p3 and increment p1 and p3
        if (nums1[p1] < nums2[p2]):
            result[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        # Otherwise, store the value at p2 into p3 and increment p2 and p3    
        else:
            result[p3] = nums2[p2]
            p2 += 1
            p3 += 1
    # If elements remain in nums1, store them in result
    while (p1 < len(nums1)):
        result[p3] = nums1[p1]
        p1 += 1
        p3 += 1
    # If elements remain in nums2, store them in result
    while (p2 < len(nums2)):
        result[p3] = nums2[p2]
        p2 += 1
        p3 += 1
    return result


print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))