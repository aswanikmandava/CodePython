"""
Given an array of integers, nums, and an integer value, target, 
determine if there are any three integers in nums whose sum is equal to the target, 
that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. 
Otherwise, return FALSE.

Pseudo Code
-----------
    a) Sort the input array in ascending order
    b) Iterate over the entire sorted array to find the triplet whose sum is equal to the target
    c) In each iteration, make a triplet by storing the current array element and the other two elements
        using two pointer (low and high), and calculate their sum
    d) Adjust the calculated sum value, until it becomes equal to the target value, 
        by conditionally moving the pointers, low and high
    e) Return TRUE if the required sum is found. Otherwise, return FALSE

Time complexity
    Sorting the list takes O(nlogn)
    O(n2)
    Total: O(nlogn) + O(n2) which simplifies to O(n2)

Space complexity
The space complexity of this solution can range from O(log(n)) to O(n), as per the sorting algorithm we use. 
We use the built-in Python function, sort(), so the space complexity of the provided solution is O(n)
.    
"""


def find_sum_of_3(nums, target):
    # sort the numbers
    nums.sort()
    print(f"Sorted: {nums}")
    num_count = len(nums)
    for i in range(num_count-2):
        low = i + 1
        high = num_count - 1
        while (low < high):
            print(f"current={nums[i]}, low={nums[low]}, high={nums[high]}")
            total = nums[i] + nums[low] + nums[high]
            print(f"total={total}")
            if total < target:  # move forward the low pointer
                low += 1
            elif total == target:
                print(f"Found match")
                return True
            else:   # move backwards the high pointer
                high -= 1

nums = [1, 2, 4, 6, 8, 20]
target = 31
nums = [2, 4, 2, 7, 6, 3, 1]
target = 18

find_sum_of_3(nums=nums, target=target)


