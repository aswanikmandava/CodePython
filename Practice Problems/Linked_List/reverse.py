# reverse the linkedlist with out using additional data structure
"""
1) Initialize three pointers: previous, next_node, and current. 
The previous and next_node pointers are initialized as NULL, while the current pointer is initialized to the head of the linked list.
2) Iterate over the linked list. While iterating, perform the following steps:
    Before changing the next pointer of current, store the next node in next_node to prevent losing the reference to the rest of the list.
    Update the next pointer of current to point to the previous node. This effectively reverses the pointer of the current node.
    Move previous to current and current to next_node to move to the next iteration.
3) After reversing the whole linked list, we’ll change the head pointer to the previous pointer because previous will be pointing to the new head node.
"""
from LinkedList import LinkedList

class LinkedListV2(LinkedList):
    def __init__(self):
        super().__init__()
    def reverse(self):
        # init 3 pointers
        previous = None     # to keep track of previous node
        current = self.head # to keep track of current node
        next = None         # to keep track of next node
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        self.head = previous
        return self.head

mylist = LinkedListV2()
print("LinkedList print at the beginning")
print(f"Init Length: {len(mylist)}")
mylist.print_list()
# insert a bunch of nodes
for i in range(1, 8):
    mylist.insert_at_head(i)

print("LinkedList print after inserting a bunch of nodes")
print("-------------------------------------------------")
mylist.print_list()
mylist.reverse()
print("LinkedList print after reverse operation")
print("-------------------------------------------------")
mylist.print_list()

