class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None    # pointer to the first node
    
    def get_head(self):
        return self.head
    
    def insert_at_head(self, data):
        new_node = Node(data)   # create a new node
        new_node.next = self.head   # new node points to the same node as head
        self.head = new_node    # point head to the new node
        return self.head
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return self.head
        # traverse the list to the end node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        return self.head

    def search(self, value):
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                return True
            cur_node = cur_node.next
        return False

    def delete_at_head(self):
        if self.is_empty():
            return
        first_node = self.head
        next_node = first_node.next
        self.head = next_node
        first_node.next = None
    
    def delete_at_tail(self):
        if self.is_empty():
            return
        # traverse the list to the end node
        cur_node = self.head
        prev_node = None
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = None

    def delete_node(self, value):
        cur_node = self.head
        prev_node = None
        deleted = False
        while cur_node:
            if cur_node.data == value:
                prev_node.next = cur_node.next
                cur_node.next = None
                deleted = True
                break
            prev_node = cur_node
            cur_node = cur_node.next
        # print(f"cur node: {cur_node.data}, prev_node: {prev_node.data}")
        return deleted

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
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
    
mylist = LinkedList()
print("LinkedList print at the beginning")
mylist.print_list()
# insert a bunch of nodes
for i in range(1, 8):
    mylist.insert_at_head(i)

print("LinkedList print after inserting a bunch of nodes")
print("-------------------------------------------------")
mylist.print_list()

print("Adding a new node at tail")
mylist.insert_at_tail(8)

print("LinkedList print after inserting a node at tail")
print("-----------------------------------------------")
mylist.print_list()

mylist.delete_at_tail()
print("LinkedList print after deleting a node at tail")
print("-----------------------------------------------")
mylist.print_list()

mylist.delete_node(5)
print("LinkedList print after deleting a node at tail")
print("-----------------------------------------------")
mylist.print_list()