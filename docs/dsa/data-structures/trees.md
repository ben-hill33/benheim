# Binary Trees and Binary Search Trees

A Tree is a node based data structure, but within a tree, each node can have links to _multiple_ nodes rather than just one like a linked list.
As in a family tree, a node can have _descendants_ and _ancestors_.

- A node's descendants are **all** the nodes that stem from a node, while a node's ancestors are **all** the nodes it stems from.
- A binary tree is a tree in which each node has zero, one, or two children
- a binary _search_ tree is a binary tree that also abides by the following rules:
  - Each node can have at most one "left" child and one "right" child.
  - A node's "left descendants can only contain values that are less than the node itself. Likewise, a node's "right" descendants can only contain values that are greater than the node itself.
  - Because of the unique structure of a binary search tree, we can search for any value within it very quickly

_The algorithm for searching with a binary search tre is as follows:_

1. Designate a node to be the "current node." At the beginning of the algorithm, the root node is the first "current node."
2. Inspect the value at the current node.
3. If We've found the value we're looking for, great!
4. If the value we're looking for _is less_ than the current node, _search for it in its left subtree_
5. If the value we're looking for _is greater_ than the current node, _search for it in its right subtree_
6. Repeat steps 1-5 until we find the value we're searching for, or until we hit the bottom of the tree, in which case our value must not be in the tree.

#### Common Terminology

- _Root_
  - The root is the first/top Node in the tree
- _Node_
  - A node is the individual item/data that makes up the data structure
- Parent 
  - A node connected to another node when moving towards the root
- Descendant 
  - a node reachable by repeated processing from parent to child
- Ancestor 
  - a node reachable by repeated processing from child to parent
- _Left Child_
  - The node that is positioned to the left of a root or node (left = <)
- _Right Child_
  - The node that is positioned to the right of a root or node (right = >)
- _Edge_
  - The edge in a tree is the link between a parent and child node
- _Leaf_
  - A leaf is a node that does not contain any children
- _Height_
  - The height of a tree is determined by the number of edges from the root to the bottommost node
- _Depth_
  - the depth of a node is the number of edges from the node to the tree’s root node
- Degree 
  - the number of sub trees of a node
- Subtree 
  - of a tree T is a tree consisting of a node in T and all of it’s descendants in T

## Tree types
### Binary Tree
Is a tree data structure in which each node has at most two children
- Full Binary tree: every node in the tree has 0 or 2 children
- Perfect binary tree: all interior nodes have two children and all leaves have the same depth or level
- Complete binary tree: every level except possibly the last is completely filled, and all nodes in the last level are as far left as possible

Depth-first search
In a depth-first search, the search is deepened as much as possible on each child before going to the next sibling

Pre-Order
Display data of root
Traverse left subtree calling preorder function
Traverse right subtree calling preorder function
In-Order
Traverse left subtree calling preorder function
Display data of root
Traverse right subtree calling preorder function
An In-Order search will return the sorted contents of a BST (Binary Search Tree)

Post-Order
Traverse left subtree calling preorder function
Traverse right subtree calling preorder function
Display data of root
A stack can be used to perform a depth-first search

#### Pointer-based
Store references to the parent and chilren
### Binary Search Tree
Or BST, is a data structure that keeps its keys in sorted order, so that operations can take advantage of the binary search principle (logarithmic search that )

#### Vocab

- [_Recursion_](https://en.wikipedia.org/wiki/Recursion)
  - occurs when a thing is defined in terms of itself or of its type.
    - _In computer science:_ A common method of simplification is to divide a problem into subproblems of the same type (divide and conquer). Recursion is exemplified when a function is defined in terms of simpler, often smaller versions of itself. The solution is then devised by combining the solutions obtained from the simpler versionf of the problem. One example application of recursion is in parsers.


#### Resources

- [_For Code Implementation_](https://www.geeksforgeeks.org/implementation-binary-search-tree-javascript/)
- [npm: binary search tree](https://www.npmjs.com/search?q=binary%20search%20tree)
- [functional red black tree npm](https://www.npmjs.com/package/functional-red-black-tree)

  
