# Given a singly linked list, remove the nth node from the end of the list and return its head.
# Pseudo code:
#   1) Set two pointers, left and right at the head of the linked list
#   2) Move the right pointer n steps forward
#   3) Move both the right and left pointers forward until right pointer reaches the last node. 
#       At this point, the left pointer will be pointing to the node behind the nth last node
#   4) Relink the left node to the node next to left's next node
#   5) Return the head of the linked list

#
# The time complexity is O(n) is the number of nodes in the linked list.
# Space complexity is O(1) because we use constant space to store two pointers.

# Template for linkedlist node class
class LinkedListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def remove_nth_last_node(head, n):
    # have 2 pointers to head
    left = head
    right = head

    # move right pointer n steps forward
    for _ in range(n):
        if right.next:
            right = right.next
            print(f"right moved to {right.data}")
    
    # move both pointers forward 1 step at a time until right pointer reaches the end
    while right.next:
        left = left.next
        right = right.next

    # The right pointer has reached the lastnode. The left pointer has reached one node before the nth last node.
    # point left node to the node after the next
    left.next = left.next.next

    return head


my_list = [23, 89, 10, 5, 67, 39, 70, 28]
# for i in range(len(my_list)):
#     print(my_list[i], end=" ")
linked_list = LinkedList()
linked_list.create_linked_list(my_list)
print(f"Original: {linked_list}")
remove_nth_last_node(linked_list.head, 4)
print(f"Updated: {linked_list}")