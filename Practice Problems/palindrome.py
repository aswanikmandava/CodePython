"""
Identify if a given string is a palindrome.
A palindrome string reads the same forwards as well as backwards

eg: racecar, abcdcba
"""

def is_palindrome(input_str):
    """
    Time complexity: O(n)
        As we iterate through every char in the string
    Space complexity: O(1)
        As we use 2 constants only
    """
    # define 2 pointers - one for the start and the other for the end
    start = 0
    end = len(input_str) - 1
    while start < end:
        if input_str[start] != input_str[end]:
            return False
        # update pointers
        start += 1
        end -= 1
    return True


# another approach
# reverse the string and compare with original string
def is_palindrome_v2(str):
    if not str:
        return False
    # the slice statement [::-1] means start at the end of the string and end at position 0, 
    # move with the step -1, negative one, which means one step backwards.
    reverse_str = str[::-1]
    if str == reverse_str:
        return True
    return False




given_str = 'hello'
given_str = 'racecar'
given_str = 'abcdcba'
print(is_palindrome_v2(given_str))