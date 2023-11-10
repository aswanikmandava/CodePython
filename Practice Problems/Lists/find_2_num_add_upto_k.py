# Given a list and a number "k", find two numbers from the list that sum to "k".

# 1) Brute Force
# Since we iterate over the entire list of n elements, n times in the worst case, 
# therefore, the time complexity is O(n2)
def find_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and (lst[i] + lst[j]) == k:
                return lst[i], lst[j]

# 2) Sort the list and use binary search
# For each element in the sorted list, use a binary search to look for the difference between that element and the intended sum. 
# You can implement the binary_search function however you like, recursively or iteratively. 
# So, if the intended sum is n and the first element of the sorted list is a0, then you will conduct a binary search for 
# n-a0 and so on for every a, i.e., an until one is found.

# Time complexity: O(nlogn)
def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            found = mid
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

isum = 45
lst = [1, 3, 10, 20, 25]
for i in lst:
    found = binary_search(lst, (isum - i))
    print(f"{i}: search for {(isum - i)} result: {found}")
    if found:
        print(f"Items {i} and {lst[found]} add upto {isum}")
        break

# 3) Dictionary
# Time complexity: O(n)
lookup = dict()
for i in lst:
    try:
        diff = (isum - i)
        lookup[diff]
        print(f"found: {i} and {diff} add upto {isum}")
    except:
        lookup[i] = 0


# 4) Using set
def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    found_values = set()
    for ele in lst:
        if n - ele in found_values:
            return [n - ele, ele]
        found_values.add(ele)
    return False

# moving indices
# The linear scan takes O(n) and sort takes O(nlogn). 
# The time complexity becomes O(nlogn)+O(n) because the sort and the linear scan are done one after the other. 
# The overall would be O(nlogn) in the worst case.
def find_sum(lst, k):
    lst_len = len(lst)
    first = 0   # index to the beginning of list
    last = lst_len - 1   # index to the end of list
    lst.sort()  # sort the list
    sum = 0
    found = False
    while (first != last and not found):
        sum = lst[first] + lst[last]
        if (sum < k):
            first += 1  # move forward
        elif (sum > k):
            last -= 1   # move backwards
        else:
            found = True
            return [lst[first], lst[last]]
    return found
    


mylist = [1, 21, 3, 14, 5, 60, 7, 6]