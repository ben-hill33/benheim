# [A beginner's guide to Big O](https://www.educative.io/blog/a-big-o-primer-for-beginning-devs?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=blog-dynamic&gclid=Cj0KCQiA2af-BRDzARIsAIVQUOd2WHUlK88GyHKEMb_aLpirfK66O4kx2MFTV0KRK7yfxJL3TOxhG9YaAmd7EALw_wcB#common)

Big O notation is used in Computer Science to describe the performance or complexity of an algorithm.
- Specifically it describes the worst-case scenario
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

  
