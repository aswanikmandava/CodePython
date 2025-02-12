def find_index(mylist, key):
    """
    Takes a list of integers and a key to find in the list
    """
    num_index = -1
    for idx in range(len(mylist)):
        if mylist[idx] == key:
            num_index = idx
    return num_index


if __name__ == "__main__":
    num_list = [20, 55, 30, 100, 30, 12, 2]
    search_num = 13

    num_index = find_index(num_list, search_num)
    print(f"Index: {num_index}")