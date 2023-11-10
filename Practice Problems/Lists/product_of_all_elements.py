# Given a list, modify it so that each index stores the product of all elements in the list 
# except the element at the index itself.

# input: [1, 2, 3, 4]
# output: [24, 12, 8, 6]

# input: [4, 2, 1, 5, 0]
# output: [0, 0, 0, 0, 40]

# time complexity: O(n2)
def find_product(lst):
    result = list()
    ind1 = 0
    while (ind1 < len(lst)):
        ind2 = 0
        product = 1
        while(ind2 < len(lst)):
            if ind1 != ind2:
                product *= lst[ind2]
                # print(f"ind1={ind1} ind2={ind2} val={lst[ind2]} prod={product}")
            ind2 += 1
        result.append(product)
        ind1 += 1
    return result

print(find_product([1, 2, 3, 4]))