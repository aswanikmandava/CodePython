
# time complexity: O(n*n) = O(n2)
# space complexity: O(1)
def insertionSort(arr):
	n = len(arr) # Get the length of the array
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return
	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

def insertion_sort_debug(lst):
    for i in range(1, len(lst)):
        j = i - 1
        key = lst[i]
        print(f"i={i}, key={key}, j={j}, list: {lst}")
        while ( j >= 0 and key < lst[j]):
            tmp = j+1
            print(f"j={j}, {key} < {lst[j]}, {lst[tmp]} changed to {lst[j]}")
            lst[j+1] = lst[j]
            j -= 1
            print(f"list state: {lst} {key} < {lst[j]}")
        print(f"j={j}, list state before assigning back key: {lst}")
        lst[j+1] = key
        print(f"list state change at position ({(j+1)}) after assigning back key: {lst}")
    return lst

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [13, 12, 11, 5, 6, 0, -1, -6]
insertionSort(arr)
print(arr)