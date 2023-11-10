"""
Merge sort is a recursive divide & conquer algorithm that essentially divides a given list into two halves, sorts those halves, 
and merges them in order. The base case is to merge two lists of size 1 so, eventually, single elements are merged in order; 
the merge part is where most of the heavy lifting happens.
"""
def merge_sort(lst):
    num_elements = len(lst)
    if num_elements <= 1:
        return
    middle = num_elements // 2
    left = lst[:middle]
    right = lst[middle:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while ( i < len(left) and j < len(right)):
        if left[i] > right[j]:
            lst[k] = right[j]
            j += 1
        else:
            lst[k] = left[i]
            i += 1
        k += 1
    # take care of elements in the left
    while (i < len(left)):
        lst[k] = left[i]
        i += 1
        k += 1
    # take care of elements in the right
    while (j < len(right)):
        lst[k] = right[j]
        j += 1
        k += 1

def merge_sort_debug(lst):
    print(f"processing {lst}")
    num_elements = len(lst)
    if num_elements <= 1:
        return
    middle = num_elements // 2
    left = lst[:middle]
    right = lst[middle:]
    print(f"Calling sort on left half: {left}")
    merge_sort_debug(left)
    print(f"Calling sort on right half: {right}")
    merge_sort_debug(right)
    print(f">>>>>>>>> left: {left}, right: {right}, list: {lst}")
    # print(f"left: {left}, right: {right}")
    i = j = k = 0
    while (i < len(left) and j < len(right)):
        if left[i] > right[j]:
            print(f"i={i},j={j},k={k},{left[i]} > {right[j]}, {lst[k]} = {right[j]}")
            lst[k] = right[j]
            j += 1
        else:
            print(f"i={i},j={j},k={k},{left[i]} <= {right[j]}, {lst[k]} = {left[i]}")
            lst[k] = left[i]
            i += 1
        k += 1
    print(f"i={i},j={j},k={k} Initial replacement, list: {lst}")
    # Checking if any element was left
    print(f"i={i},j={j},k={k} processing left, list: {lst}")
    while (i < len(left)):
        lst[k] = left[i]
        print(f"i={i},j={j},k={k}, {lst[k]} = {left[i]}")
        i += 1
        k += 1
    print(f"i={i},j={j},k={k} processing right, list: {lst}")
    # Checking if any element was left
    while (j < len(right)):
        lst[k] = right[j]
        print(f"i={i},j={j},k={k}, {lst[k]} = {right[j]}")
        j += 1
        k += 1
    print(f"<<<<<<<< list: {lst}")
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    lst = [30, 2, -1, 15, 4, -6, 24, 8, -3]
    # merge_sort_debug(lst)  # Calling selection sort function
    merge_sort(lst)
    # Printing Sorted lst
    print("Sorted lst: ", lst)

"""
processing [30, 2, -1, 15, 4, -6, 24, 8, -3]
Calling sort on left half: [30, 2, -1, 15]
processing [30, 2, -1, 15]
Calling sort on left half: [30, 2]
processing [30, 2]
Calling sort on left half: [30]
processing [30]
Calling sort on right half: [2]
processing [2]
>>>>>>>>> left: [30], right: [2], list: [30, 2]
i=0,j=0,k=0,30 > 2, 30 = 2
i=0,j=1,k=1 Initial replacement, list: [2, 2]
i=0,j=1,k=1 processing left, list: [2, 2]
i=0,j=1,k=1, 30 = 30
i=1,j=1,k=2 processing right, list: [2, 30]
<<<<<<<< list: [2, 30]
Calling sort on right half: [-1, 15]
processing [-1, 15]
Calling sort on left half: [-1]
processing [-1]
Calling sort on right half: [15]
processing [15]
>>>>>>>>> left: [-1], right: [15], list: [-1, 15]
i=0,j=0,k=0,-1 <= 15, -1 = -1
i=1,j=0,k=1 Initial replacement, list: [-1, 15]
i=1,j=0,k=1 processing left, list: [-1, 15]
i=1,j=0,k=1 processing right, list: [-1, 15]
i=1,j=0,k=1, 15 = 15
<<<<<<<< list: [-1, 15]
>>>>>>>>> left: [2, 30], right: [-1, 15], list: [30, 2, -1, 15]
i=0,j=0,k=0,2 > -1, 30 = -1
i=0,j=1,k=1,2 <= 15, 2 = 2
i=1,j=1,k=2,30 > 15, -1 = 15
i=1,j=2,k=3 Initial replacement, list: [-1, 2, 15, 15]
i=1,j=2,k=3 processing left, list: [-1, 2, 15, 15]
i=1,j=2,k=3, 30 = 30
i=2,j=2,k=4 processing right, list: [-1, 2, 15, 30]
<<<<<<<< list: [-1, 2, 15, 30]
Calling sort on right half: [4, -6, 24, 8, -3]
processing [4, -6, 24, 8, -3]
Calling sort on left half: [4, -6]
processing [4, -6]
Calling sort on left half: [4]
processing [4]
Calling sort on right half: [-6]
processing [-6]
>>>>>>>>> left: [4], right: [-6], list: [4, -6]
i=0,j=0,k=0,4 > -6, 4 = -6
i=0,j=1,k=1 Initial replacement, list: [-6, -6]
i=0,j=1,k=1 processing left, list: [-6, -6]
i=0,j=1,k=1, 4 = 4
i=1,j=1,k=2 processing right, list: [-6, 4]
<<<<<<<< list: [-6, 4]
Calling sort on right half: [24, 8, -3]
processing [24, 8, -3]
Calling sort on left half: [24]
processing [24]
Calling sort on right half: [8, -3]
processing [8, -3]
Calling sort on left half: [8]
processing [8]
Calling sort on right half: [-3]
processing [-3]
>>>>>>>>> left: [8], right: [-3], list: [8, -3]
i=0,j=0,k=0,8 > -3, 8 = -3
i=0,j=1,k=1 Initial replacement, list: [-3, -3]
i=0,j=1,k=1 processing left, list: [-3, -3]
i=0,j=1,k=1, 8 = 8
i=1,j=1,k=2 processing right, list: [-3, 8]
<<<<<<<< list: [-3, 8]
>>>>>>>>> left: [24], right: [-3, 8], list: [24, 8, -3]
i=0,j=0,k=0,24 > -3, 24 = -3
i=0,j=1,k=1,24 > 8, 8 = 8
i=0,j=2,k=2 Initial replacement, list: [-3, 8, -3]
i=0,j=2,k=2 processing left, list: [-3, 8, -3]
i=0,j=2,k=2, 24 = 24
i=1,j=2,k=3 processing right, list: [-3, 8, 24]
<<<<<<<< list: [-3, 8, 24]
>>>>>>>>> left: [-6, 4], right: [-3, 8, 24], list: [4, -6, 24, 8, -3]
i=0,j=0,k=0,-6 <= -3, 4 = -6
i=1,j=0,k=1,4 > -3, -6 = -3
i=1,j=1,k=2,4 <= 8, 24 = 4
i=2,j=1,k=3 Initial replacement, list: [-6, -3, 4, 8, -3]
i=2,j=1,k=3 processing left, list: [-6, -3, 4, 8, -3]
i=2,j=1,k=3 processing right, list: [-6, -3, 4, 8, -3]
i=2,j=1,k=3, 8 = 8
i=2,j=2,k=4, 24 = 24
<<<<<<<< list: [-6, -3, 4, 8, 24]
>>>>>>>>> left: [-1, 2, 15, 30], right: [-6, -3, 4, 8, 24], list: [30, 2, -1, 15, 4, -6, 24, 8, -3]
i=0,j=0,k=0,-1 > -6, 30 = -6
i=0,j=1,k=1,-1 > -3, 2 = -3
i=0,j=2,k=2,-1 <= 4, -1 = -1
i=1,j=2,k=3,2 <= 4, 15 = 2
i=2,j=2,k=4,15 > 4, 4 = 4
i=2,j=3,k=5,15 > 8, -6 = 8
i=2,j=4,k=6,15 <= 24, 24 = 15
i=3,j=4,k=7,30 > 24, 8 = 24
i=3,j=5,k=8 Initial replacement, list: [-6, -3, -1, 2, 4, 8, 15, 24, -3]
i=3,j=5,k=8 processing left, list: [-6, -3, -1, 2, 4, 8, 15, 24, -3]
i=3,j=5,k=8, 30 = 30
i=4,j=5,k=9 processing right, list: [-6, -3, -1, 2, 4, 8, 15, 24, 30]
<<<<<<<< list: [-6, -3, -1, 2, 4, 8, 15, 24, 30]
Sorted lst:  [-6, -3, -1, 2, 4, 8, 15, 24, 30]
"""