"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution_1:
    """
    Time complexity: O(n)
        As we iterate through every node in the list
    Space complexity: O(1)
        It is constant as we only create 2 pointer for every size of the given list
        we don't create a data structure proportional in size to the number of nodes in our list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # create 2 pointers each pointing to head of the given linkedlist
        low = high = head
        while high and high.next:
            # advance low pointer by 1 step and the high pointer by 2 steps
            low.next = low.next
            high.next = high.next.next
        return low


class Solution_2:
    def middle_node(self, head: ListNode) -> ListNode:
        node_count = 0
        dummy_head = head
        while dummy_head:
            node_count += 1
            dummy_head = dummy_head.next
        for num in range(node_count // 2):
            head = head.next
        return head

class Solution_3:
    """
    Iterate through each node in the linkedlist and append the head to a list
    Floor divide its length by 2 to get a middle node

    Time complexity: O(n)
    Space complexity: O(n)
        As created a list of equal size to all the nodes in our list
    """
    def midle_node(self, head: ListNode) -> ListNode:
        node_count = 0
        node_list = []
        while head:
            node_count += 1
            node_list.append(head)
            head = head.next
        return node_list[node_count//2]



# test cases
def test_middle_node():
    pass