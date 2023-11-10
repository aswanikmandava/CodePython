# https://www.educative.io/answers/how-to-implement-quicksort-in-python
"""
The algorithm can be broken down into three parts:
    1) Partitioning the array about the pivot.
    2) Passing the smaller arrays to the recursive calls.
    3) Joining the sorted arrays that are returned from the recursive call and the pivot.
"""
def QuickSort(arr):

    elements = len(arr)
    
    #Base case
    if elements < 2:
        return arr
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Brings pivot to it's appropriate position
    
    left = QuickSort(arr[0:current_position]) #Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr

def quick_sort_debug(arr):
    elements = len(arr)
    #Base case
    if elements < 2:
        return arr
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
        print(f"i={i} lst: {arr}")
        if arr[i] <= arr[0]:
            current_position += 1
            print(f"pos={current_position}, {arr[i]} <= {arr[0]}, pos ele: {arr[current_position]}")
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp
            print(f"After swap - lst: {arr}")
    print(f"Change pivot from {arr[0]} to {arr[current_position]}")
    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Brings pivot to it's appropriate position

    
    left = quick_sort_debug(arr[0:current_position]) #Sorts the elements to the left of pivot
    right = quick_sort_debug(arr[current_position+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr

array_to_be_sorted = [10,4,2,7,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",quick_sort_debug(array_to_be_sorted))