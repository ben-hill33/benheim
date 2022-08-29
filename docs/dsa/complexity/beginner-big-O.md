## :material-run-fast: The Speed of Algorithms

Big O notation is used in Computer Science to describe the performance or complexity of an algorithm.

- Big O describes the worst-case, or slowest, scenario as we consider how many steps an algorithm should take. If it takes many steps, how will the algorithm scale with a company as it grows? In other words
- Can be used to describe execution time required or the space used

## Vocab

- **O(1):** _Constant time complexity_ - translates to a constant runtime, meaning regardless of the size of the input, the algorithm will have the same runtime.
  - Example: Array, inserting or retrieving an element
- **O(n):** _Linear time complexity_ - describes an algorithm whose performance will grow linearly and in direct proportion to the size of the input data set. This means it will have loops that iterate over an unkown (n) amount of items
  - Example: Tree - Depth first search 
- **O(log N):** _Logarithmic time complexity_ - means that time goes up linearly, while the n goes up exponentially. So if it takes 1 second to traverse through 10 elements, it will take 2 to read 100 elements etc. 
  - _Divide and Conquer algorithms_ 
  - Example: Binary tree - inserting or retrieving an element
- **O(n2):** _Quadratic time complexity_ - As the elements in your list increase, the time it will take for your algorithm to run will increase exponentially.
  - Example: _Sorting Algorithm_ - Bubble Sort and insertion sort

  
