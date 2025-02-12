def find_max_ele(mylist):
    """
    Find index of minimum element
    """
    max_ele = float("-inf")
    for idx in range(len(mylist)):
        if mylist[idx] > max_ele:
            max_ele = mylist[idx]
    return max_ele


if __name__ == "__main__":
    num_list = [20, 55, -30, 100, 30, 1299, 2]

    max_ele = find_max_ele(num_list)
    print(f"Index: {max_ele}")