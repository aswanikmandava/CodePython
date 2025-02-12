def find_min_ele(mylist):
    """
    Find index of minimum element
    """
    min_ele = float("inf")
    for idx in range(len(mylist)):
        if mylist[idx] < min_ele:
            min_ele = mylist[idx]
    return min_ele


if __name__ == "__main__":
    num_list = [20, 55, -30, 100, 30, 12, 2]

    min_ele = find_min_ele(num_list)
    print(f"Index: {min_ele}")