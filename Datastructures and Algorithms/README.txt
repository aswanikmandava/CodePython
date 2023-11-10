Hashing refers to the process of generating a fixed-size output from an input of variable size using the mathematical formulas known as 
hash functions. This technique determines an index or location for the storage of an item in a data structure.

A tree data structure is a hierarchical structure that is used to represent and organize data in a way that is easy to navigate and search. 
It is a collection of nodes that are connected by edges and has a hierarchical relationship between the nodes. 
The topmost node of the tree is called the root, and the nodes below it are called the child nodes. 
Each node can have multiple child nodes, and these child nodes can also have their own child nodes, forming a recursive structure.

Binary tree – This is a special type of tree where each node can have a maximum of 2 children.
Complete Binary Tree – In this type of binary tree all the levels are filled except maybe for the last level. But the last level elements are filled as left as possible.
Perfect Binary Tree – A perfect binary tree has all the levels filled
Binary Search Tree – A binary search tree is a special type of binary tree where the smaller node is put to the left of a node and a higher value node is put to the right of a node

Tree Traversal (In Order)
==============
Traverse the left subtree, i.e., call Inorder(left->subtree)
Visit the root.
Traverse the right subtree, i.e., call Inorder(right->subtree)

Tree Traversal (Pre Order)
==============
Visit the root.
Traverse the left subtree, i.e., call Preorder(left->subtree)
Traverse the right subtree, i.e., call Preorder(right->subtree)

Tree Traversal (Post Order)
==============
Traverse the left subtree, i.e., call Postorder(left->subtree)
Traverse the right subtree, i.e., call Postorder(right->subtree)
Visit the root
