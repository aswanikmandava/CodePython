# Given a list, find the first integer which is unique in the list. 
# Unique means the number does not repeat and appears only once in the whole list.

# Brute Force
# time complexity: O(n2)
def find_first_unique(lst):
    i = 0
    while (i < len(lst)):
        j = 0
        found = None
        while( j < len(lst)):
            if (i != j and lst[i] == lst[j]):
                found = True
                break
            j += 1
        if not found:
            return lst[i]
        i += 1
    return

# Brute Force (revised)
def find_first_unique(lst):
    num_elements = len(lst)
    for i in range(num_elements):
        j = 0
        found = None
        while ( j < num_elements):
            if (i != j and lst[i] == lst[j]):
                found = True
                break
            j += 1
        if not found:
            return lst[i]
    return
print(find_first_unique([4,5,1,2,0,4]))