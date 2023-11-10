# Given a list of size 'n', find the minimum value in the list
def find_minimum(arr):
    min = arr[0]
    i = 1
    while (i < len(arr)):
        if (min > arr[i]):
            min = arr[i]
        i += 1
    return min


print(find_minimum([4,2,1,5,0]))