# [Linked Lists](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html)

Node based data structures that offer new ways to organize and access data that provide a number of major performance advantages. 

Like an array, a linked list is a data structure that represents a list of items. While on the surface, arrays and linked lists look and act quite similarly, there are big differences under the hood. 
- Instead of being a contiguous block of memory (arrays), the data from linked lists can be scattered across different cells through the computer's memory.
- Connected data that is dispersed throughout memory are known as _nodes_
- In a linked list, each node represents one item in the list

- **If the nodes are not next to each other in memory, how does the computer know which nodes are part of the same linked list?**
  - This question is the key to the linked list
  - each node also comes with the memory address of the _next_ node in the list. 
  - each node consists of two memory cells
    - the first cell holds the actual data (**head**)
    - the second cell serves as a link that indicates where in memory the next node begins
  - the final node's link contains **null** since the link list ends there (**tail**)
- If the computer knows at which memory address the linked list begins, it has all it needs to begin working with the list

The fact that a linked list's data can be spread throughout the computer's memory is a potential advantage it has over an array. An array, by contrast, needs to find an entire block of contiguous cells to store its data, which can get inscreasingly difficult as the array size grows. 

### Efficiency
**O(n)**
Linked lists are most powerful when using _insertion_ and _deletion_ methods which have O(1)

### Implementation

- best way to approach a traversal is through the use of a while() loop. Allowing us to continually check that the Next node in the list is not null. A NullReferenceException gets thrown and our program will crash/end.
- Regardless of the language we start to program in, one of the first things that we encounter are data structures.

### Vocab

-   **_data structures_** - A way we can organize our data, variables, arrays, hashes, and objects are all types of data structes.
-  _Node_ - Nodes are pieces of data that may be dispersed throughout the computer's memory. 
-  **_Singly_** - Singly refers to the number of references the node has. A singly linked list means that there is only one reference, and the reference points fo the Next node in a linked list.
-  **_Doubly_** - Refers to there being two references within the node. A doubly linked list means that there is a reference to both the next and previous node.
-  **_next_** - Each node contains a property called Next. This property contains the reference to the next node.
-  **_head_** - is a reference type of node to the first node in a linked list.
-  **_current_** - is a reference type of type node that is currently being looked at. This node is traditionally used when traversing through a full linked list. When traversing, you typically reset the current to the head to guarantee you are starting from the beginning of the linkedl list.



### Resources
- [What's a Linked list, Anyway? Part 1](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
- [What's a Linked List, Anyway? Part 2](https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996)



[Table of Contents](../index.md)
