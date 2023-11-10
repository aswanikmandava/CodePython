"""
Implement a function sort_binary_list(lst) that takes a binary list of numbers and returns a sorted list.

Input
A list having binary numbers

Output
A sorted binary list

Sample Input
lst = [1, 0, 1, 0, 1, 1, 0, 0]

Sample Output
result = [0, 0, 0, 0, 1, 1, 1, 1]
"""

# Solution-1 - (Bubble Sort)
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

# Solution-2 - (Swapping 1's)
"""
We are pushing all ones towards the right and all the zeros towards the left. 
For this, we have maintained two variables i and j. The index i moves forward in the list and finds out if the element at 
index i is zero. If it is, it swaps it with the element at index j. Index j is keeping track of the last position where 
we have placed our last zero element in the list. As soon as we swap, we move the index j ahead to the next index, where 
zero can be placed in the next swap.

Time complexity
    Since the list is iterated only once, the time complexity is O(n)
"""

def sort_binary_list(lst):
    j = 0
    for i in range(len(lst)):
        if lst[i] < 1:
            print(f"Swap i={i}, j={j}")
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
        print(f"iter complete i={i} j={j}; {lst}")


if __name__ == '__main__':
    lst = [1, 0, 1, 0, 1, 1, 0, 0]
    sort_binary_list(lst)
    print(lst)