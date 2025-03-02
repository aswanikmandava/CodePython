class Node:
    def __init__(self, data):
        self.data = data    # stores data
        self.prev = None    # stores the pointer to the previous node
        self.next = None    # stores the pointer to the next node

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return self.head
        first_node = self.head
        first_node.prev = new_node
        new_node.next = first_node
        self.head = new_node
        return self.head
    
    def print_list(self):
        if self.is_empty():
            print("DoubleLinkedList is empty")
            return False
        temp = self.head
        while temp.next is not None:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print(f"{temp.data} -> None")
        return True
    
mylist = DoubleLinkedList()
print("Double LinkedList print at the beginning")
mylist.print_list()
# insert a bunch of nodes
for i in range(1, 10):
    mylist.insert_at_head(i)

print("DoubleLinkedList print after inserting a bunch of nodes")
print("-------------------------------------------------")
mylist.print_list()