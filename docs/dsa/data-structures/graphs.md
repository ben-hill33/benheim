# [Graphs](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/graphs.html)

Graphs are a more general structure than trees, and in fact, we can think of a tree as a special kind of graph. 
- A graph is a non-linear data structure that can be looked at as a collection of vertices potentially connected by line segments called edges 

## Vocab
- _Vertex_
  - AKA a node, is a fundamental part of a graph
  - Each node can have a name, or key, and can also have additional information, or payload
- _Edge_
  - Connects two vertices to show that there is a relationship between them
  - May be one-way or two-way
  - If the edges in a graph are all one-way, we say that the graph is a **directed graph**, or a **digraph**
- _Neighbor_
  - The neighbors of a node are its adjacent nodes, connected via an edge
- _Weight_
  - Edges may be weighted to show that there is a cost to go from one vertex to another
- _Path_
  - A path in a graph is a sequence of vertices that are connected by edges
- _Cycle_
  - In a directed graph is a path that starts and ends at the same vertex
  - A graph with no cycles is called an **acyclic graph**
  - A directed graph with no cycles is called a **directed acyclic graph** or DAG

An _undirected graph_ is a graph where each edge is undirected or bi-directional. Meaning the undirected graph does not move in any direction.

A _directed graph_ (digraph), is a graph where every edge is directed. 
- Each node is directed at another node with a specific requirement of what node should be referenced next

The three different types of graphs are completed, connected, and disconnected
- _Complete graphs_
  - When all nodes are connected to all other nodes
- _Connected_
  - is a graph where all nodes have at least one edge
  - A _tree_ is a form of a connected graph
- _Disconnected_
  - is a graph where some vertices may not have edges, or where some nodes aren't connected to other nodes

An _acyclic graph_ is a directed graph without cycles.
- A cycle is when a node can be traversed through and potentially end up back at itself

A _cyclic graph_ is a graph that has cycles
- A cycle is defined as a path of a positive length that starts and ends at the same vertex
- Circular

Graphs are represented through _adjacency matrix_ and _adjacency list_
- _Adjacency Matrix_ is represented through a 2 dimensional
- _Adjacency List_ is the most common way to represent graphs
  - is a collection of linked lists or array that lists all of the other vertices that are connected
  - make it easy to view if one vertices connects to another

You will be required to traverse through a graph. They're like tree traversals 

- Breadth First
  - enqueue
  - dequeue
    - if the dequeue'd node has unvisited child nodes, add the unvisited chilren to visited set and insert them into the queue

- Depth first
  - push the root node onto the stack
    - start a while loop while the stack is not empty
  - peek at the top node in the stack
  - if the top node has unvisited children, mark the toop node as visited, and then push the unvisited chilren back into the stack
  - If the top node does not have any unvisited children, pop that node off the stack
  - Repeat until the stack is empty



  
