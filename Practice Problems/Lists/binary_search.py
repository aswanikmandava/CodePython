"""
Given a list, find an item using binary search algorithm
"""
def binary_search(lst, item):
    """
    Binary Search helper function
    :param lst: A list of integers
    :param item: An item to be searched in the list
    """
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

def binary_search_r(lst, low, high, key):
    # use recursive approach
    if high < low:
        return -1
    mid = (low + high) // 2
    if lst[mid] == key:
        return mid
    if lst[mid] < key:
        return binary_search_r(lst, mid+1, high, key)
    return binary_search_r(lst, low, mid-1, key)

def binary_search_debug(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    print(f"list: {lst}")
    while (first <= last and not found):
        mid = (first + last) // 2
        print(f"first: {first}, last: {last}, mid: {mid}, mid ele: {lst[mid]}")
        if lst[mid] == item:
            found = mid
            print(f"Found {item} at index {mid}")
            return found
        if item < lst[mid]:
            print(f"{item} < {lst[mid]}, first: {first}, mid: {mid}, last: {last} adjusting last index to {(mid - 1)}")
            last = mid - 1
        else:
            print(f"{item} >= {lst[mid]}, first: {first}, mid: {mid}, last: {last} adjusting first index to {(mid + 1)}")
            first = mid + 1
    return found

if __name__ == '__main__':
    # lst = [3, 2, 1, 5, 4]
    lst = [30, 2, -1, 15, 4, -6, 24, 8, -3]
    lst.sort()
    print(binary_search(lst, 60))
