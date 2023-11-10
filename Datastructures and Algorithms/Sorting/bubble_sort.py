"""
This is another famous sorting algorithm also known as 'sinking sort'. 
It works by comparing adjacent pairs of elements and swapping them if they are in the wrong order. 
This is repeated until the list is sorted.

Think of it this way: a bubble passes over the list, 'catches' the maximum/minimum element, 
and brings it over to the right side.
"""
# time complexity: O(n*n) = O(n2)
# space complexity: O(1)
def bubble_sort(lst):
    num_elements = len(lst)
    for i in range(num_elements):
        # traverse the list from 0 to size - i - 1
        # last i elements are already in place
        for j in range(0, num_elements - i -1):
            # Swap if the element found is greater than the next element
            if (lst[j] > lst[j+1]):
                # swap elements
                lst[j], lst[j+1] = lst[j+1], lst[j]
random_list_of_nums = [1, -2, 3, 40, 5, 0, 7]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)