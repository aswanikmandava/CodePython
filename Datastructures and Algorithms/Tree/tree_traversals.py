"""
1
  -2
     -  4
     -  5
  -3
"""
# Tree node definition
class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None
    
def print_in_order(root):
    if not root:
        return
    # traverse left sub-tree
    print_in_order(root.left)
    print(root.val)
    # traverse right sub-tree
    print_in_order(root.right)

def print_pre_order(root):
    if not root:
        return
    print(root.val)
    # traverse left sub-tree
    print_pre_order(root.left)
    # traverse right sub-tree
    print_pre_order(root.right)

def print_post_order(root):
    if not root:
        return
    # traverse left sub-tree
    print_post_order(root.left)
    # traverse right sub-tree
    print_post_order(root.right)
    print(root.val)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("----- IN ORDER ---")
    print_in_order(root)
    print("----- PRE ORDER ---")
    print_pre_order(root)
    print("----- POST ORDER ---")
    print_post_order(root)