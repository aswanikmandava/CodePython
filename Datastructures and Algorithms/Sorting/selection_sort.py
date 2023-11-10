"""
This algorithm works by repeatedly finding the minimum element in the list and placing it at the beginning. 
This way, the algorithm maintains two lists:
    the sublist of already-sorted elements, which is filled from left to right
    the sublist of the remaining unsorted elements that need to be sorted
In other words, this algorithm works by iterating over the list and swapping each element with the minimum (or maximum) 
element found in the unsorted list with that in the sorted list.
"""
# time complexity: O(n*n) = O(n2)
# space complexity: O(1)

def selection_sort(lst):
    num_elements = len(lst)
    for i in  range(num_elements):
        # find the minimum element in the unsorted list
        min_index = i
        for j in range((i+1), num_elements):
            if (lst[min_index] > lst[j]):
                min_index = j
        # swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]

def selection_sort_debug(lst):
    num_elements = len(lst)
    for i in range(num_elements):
        min_index = i
        for j in range(i+1, num_elements):
            if lst[min_index] > lst[j]:
                print(f"{lst[min_index]} > {lst[j]} changed min index to {j}")
                min_index = j
            print(f"i={i}, j={j}, min_index={min_index}")
        # swap elements
        lst[i], lst[min_index] = lst[min_index], lst[i]

# Driver code to test above
if __name__ == '__main__':

    # lst = [3, 2, 1, 5, 4]
    lst = [30, 2, -1, 15, 4, -6]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)