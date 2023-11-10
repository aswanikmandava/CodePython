# Given a list of size n, can you find the second maximum element in the list

# Solution-1 (Sort and Index)
# time complexity: O(nlogn)
def insertionSort(arr):
	n = len(arr) # Get the length of the array
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return

	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			# print(f"i={i} j={j} {key} < {arr[j]}")
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

def find_second_maximum(lst):
    # sort the items
    insertionSort(lst)
    if len(lst) >= 2:
        return lst[-2]
    else:
        return None
    
# Solution (Traverse the list twice)
# time complexity: O(n)
def find_second_maximum(lst):
	# find max number
    biggest = lst[0]    # init some value
    for i in range(1, len(lst)):
        if biggest < lst[i]:
            # print(f"{biggest} < {lst[i]}")
            biggest = lst[i]
    print(f"max: {biggest}")
    # find second to max number
    max_2 = 1.0 # init some value
    for i in range(1, len(lst)):
        # print(f"{max_2} < {lst[i]}")
        if max_2 < lst[i] and lst[i] != biggest:
            max_2 = lst[i]
    print(f"2nd max: {max_2}")
    return max_2

# Solution (Traverse the list once)
# time complexity: O(n)
def find_second_maximum(lst):
    # init
    max = max_2 = -999999
    for i in range(len(lst)):
        if (max < lst[i]):
            max_2 = max # store current max into 2nd max
            max = lst[i]    # update max
        elif (lst[i] != max and max_2 < max):
            max_2 = lst[i]
    if max_2 == -999999:
        return
    else:
        return max_2
print(find_second_maximum([9,20,3,60]))
# print(find_second_maximum([1,2,2,4,4]))
