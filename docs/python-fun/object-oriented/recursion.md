## [Thinking recursively](https://realpython.com/python-thinking-recursively/)

### Recursive Functions (in Python)

A recursive function is a function defined in terms of itself via self-referential expressions

- The function will continue to call itself and repeat its behavior until some condition is met to return a result
- All recursive functions are made up of two parts:
    1. base case
        - The base case is your initial condition
    2. recursive case

!!! note "The recursive case is the idea of taking a problem and reducing it down into smaller pieces"

    As the large problem is broken down into successively less complex ones, those subproblems must eventually become so simple that they can be solved without further subdivision




For functions, each recursive call adds a stack frame (execution context) to the call stack until we reach the base case. Then the stack begins to undwind as each call returns its results.

### Maintaining State

When dealing with recursive functions, keep in mind that each recursive call has its own execution context, to maintain state during recursion you have to either:

- Thread the state through each recursive call so that the current state is part of the current call's execution context
- Keep the state in global scope
    - [For more on threading](https://realpython.com/intro-to-python-threading/)
    - [For more on namespaces and scope](https://realpython.com/python-namespaces-scope/)

### Recursive Data Structures in Python

A list is an example of a recursive data structure.

## [Recursion](https://www.geeksforgeeks.org/recursion/)

**How is a particular problem solved using recursion?**

- The idea is to represent a problem in terms of one or more smaller problems, and add one or more base conditions that stop the recursion
**What is the difference between direct and indirect recursion?**
- A function is called direct recursive if it calls the same function
- A function is indirect recursive if it calls another function and that second function calls the first function directly or indirectly 
**How is memory allocated to different function calls in recursion?**
- When any function is called from main(), the memory is allocated to it on the stack. 
- A recursive function calls itself, the memory for a called function is allocated on top of memory allocated to calling function and different copy of local variables is created for each function call.
- When the base case is reached, the function returns its value to the fucntion by whom it is called and memory is de-allocated and the process continues

??? example "Recursion examples"

    ```py
    def recursivePrint(test):
      # base case
      if test < 1:
        return
      else:
        print(test, end=" ")
        # recursive case
        recursivePrint(test - 1)
        print(test)
        return
    ```


### Vocab

- Recursion
    - The process in which a function calls itself directly or indirectly 
- Base condition
    - is the starting point of your condition. If you're looking to solve a problem where n is less than or equal to one, that is your base case: `if(n <= 1)`


### Videos
- [Intro to Modules and Packages](https://realpython.com/courses/python-modules-packages/)