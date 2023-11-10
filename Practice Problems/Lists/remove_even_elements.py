# remove even elements in a given list

# Steps
# for each element in the duplicate list
# check if element % 2 == 0
# remove element from the orig list

# time complexity: O(n) as whole list is to be iterated

def remove_even(lst):
    for item in lst[:]:
        if item % 2 == 0:
            lst.remove(item)
    return lst

def remove_even(lst):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in lst if number % 2 != 0]

# my_full_list = list(range(10))
my_full_list = [62, 138, -120, 79, 93, 175]

print(remove_even(my_full_list))