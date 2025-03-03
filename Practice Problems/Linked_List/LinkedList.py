class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def insert_at_head(self, data):
        new_node = Node(data)   # create a new node
        new_node.next = self.head   # new node points to the same node as head
        self.head = new_node    # point head to the new node
        return self.head

    def print_list(self):
        if self.is_empty():
            print("LinkedList is empty")
            return False
        temp = self.head
        while temp.next is not None:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print(f"{temp.data} -> None")
        return True

    def __len__(self):
        if self.is_empty():
            return 0
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count