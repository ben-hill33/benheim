# Stacks and Queues

## Stacks

### What is a stack?

- A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous
  - A stack stores data in the same ways that arrays do, which is a list of elements, only with the following three constraints:
    - Data can be inserted only at the end of a stack (aka pushing onto the stack)
    - Data can be deleted only from the end of a stack(aka popping from the stack)
    - Only the last element of a stack can be read
  - A handy acronym used to desribe stack operations is LIFO (last in, first out) which means that the _last_ item _pushed_ onto a stack is always the _first_ item popped from it.
    - Like a stack of dishes, you add a dish to the top of the stack, and if you were to remove a dish, you'd take the dish at the top of the stack first.

Unlike an array, most programming languages don't actually come with the stack as a built-in data type or class.

- This means a way to implement a stack would be to use a built-in array to hold the data
- If a class is built around the array, the interface forces a user to interact with the array in limited ways such as,
  - one can only read the last item where a traditional array can read any index
- The stack is really a set of rules and processes around how we should interact with an array so that we can achieve a particular result.
- All a stack cares about is that there's a list of data elements that act in a LIFO way
- Because of this, the stack is an example of an **_abstract data type_**
  - a kind of data structure that is a set of theoretical rules that revolve around some other built-in data structure

#### Why not just use an array, then?

If by definition a stack is just a constrained version of an array, that means an array can do anything a stack can do. What's the advantage of using a stack, then?

##### Stacks are important for several reasons

- When working with a constrained data structure, we can prevent potential bugs.
  - If a programmer inadvertantly writes code that removes items from the middle of an array, the algorithm will break.
  - By using a stack, we're forced into only removing items from the top, as it's impossible to get the stack to remove any other item
- Stacks give us a new mental model for tackling problems.
  - Rather than having a fixed mindset on using an array to handle certain problems where you can access any index, a stack narrows down a problem into the LIFO process
  - Using this process, we can solve all sorts of new problems we can't solve with an array
- Once we're familiar with the stack and LIFO, the code becomes familiar and elegant to other developers who read our code
  - As soon as someone sees a stack being used within an algorithm, they immediately know that the algorithm is working with a LIFO-based process

##### Stack use cases

The undo function in a word processor, for example, is a great use case for a stack.

- Each key stroke adds onto the stack
- When the undo button is hit, it pops the most recent keystroke from the stack

Another use case is reversing order

- Because the order of a stack is fixed, reverse order can be achieved very easily by popping elements off one stack and immediately onto another

`Push O(1)`

- Pushing a Node onto a stack will always be O(1) operation.
- It takes the same amount of time no matter how many Nodes you have in the stack

##### Stacks Terms

- **Push** - Nodes or items that are put into the stack are pushed
- **Pop** - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
- **Top** - This is the top of the stack.
- **Peek** - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack
- **IsEmpty** - returns true when stack is empty otherwise returns false.
- **FILO** - First In Last Out; means that the first item added in the stack will be the last item popped out of the stack.
- **LIFO** - Last In First Out; means that the last item added to the stack will be the first item popped out of the stack.

## Queues

### What is a queue?

A queue is another data structure designed to process temporary data. Think of a queue like a line of people waiting for a thing. The first person in line will be the first person to access the thing

- With queues, the first item added to the queue is the first item to be removed. Ready for the next acronym?
  - **FIFO:** or first in first out
- While stacks are viewed vertically, or top to bottom, queues are viewed horizontally
- It's also common to refer to the beginning of a queue as its front, and the end as its back
- It's also an abstract data type

Like stacks, queues are arrays with three restrictions:

- Data can be inserted only at the _end_ of a queue (just like a stack)
- Data can be deleted only from the _front_ of a queue (opposite of a stack)
- Only the element at the _front_ of a queue can be read (opposite of a stack)

Queues also wrap a built-in array like a stack with an interface that restricts our interaction with the data, allowing us to process that data in specific ways:

- The `enqueue()` method allows us to insert data at the end of the array
- The `dequeue()` method removes the first item from the array
- And the `read()` method allows us to _peek_ at just the very first element of the array

### Use cases

- Printing jobs are a common use case for queues
  - Every time a new job is added to the queue, it's added at the back
  - Every time a job is finished, it's removed from the front using the dequeue method

- Queues are also the perfect tool for handling asynchronous requests
  - They ensure that the requests are processed in the order in which they were received

- Call centers that puts callers on hold to the next available representative
