## Let's Define Abstract..

An _abstract data type, commonly referred to as an ADT_, is a data type for _objects_ where the behaviors (methods) are defined by a set of values and a set of operations. 

- The ADT lists the operations that can be performed but not how these operations will be implemented. 
- It is called abstract because it gives the list of behaviors for the data type, but the details for the implementations are hidden. 
- For example, with the _Stack ADT_, we think of the operations of `push`, `pop`, and `size`. 
  - However, the implementation of push, pop, and size can vary widely depending on the operating system and the programming language. 
  - In addition, the implementation can change over time to become more efficient. The changes will not affect the applications that use the ADT because the operation names (behaviors) do not change.
- The ADT is also _easier to use_ because the user _does not need to know how the operations are implemented_. 
  - The user simply needs to _know how the structure is generally organized_ and _what the user can do with the ADT (operations)_.

## `list` ADT

The List ADT is defined as
> a collection of items of the same type that has this format: Item[0], ltem[1], ltem[2], ..., ltem[n-1]. 

Notice that in the definition, a position or location is specified for each element. We say that the length of a list is the number of items; for example, the length of the list denoted by `l0, l1, l2, ..., ln-1` is `n`. 

Typical operations performed on lists include the following:

- Determine whether or not the list is empty.
- Find the size of the list.
- Clear the list.
- Add an item to the list at an unspecified location or at a given location.
- Remove a given item from the list.
- Remove the item at a specific location in a list.
- Search the list for a given item, and if it is there, show its location.

If you look at the operations listed in the List definition, you'll see these three: 

- remove an item (delete) 
- add an item (insert)
- and search for an item 

!!! note
    It is important to note that these operations are present not only in lists, but in many of the ADTs. In fact, one of the areas of study in the field of data structures and algorithms is the efficient implementation of these functions across the different data structures.

### Implementing a list ADT

The class ArrayList below, whose source code is provided at the end, implements four operations and three getters. To simplify our example, a number of potential operations, such as clear the list or search the list, have been left out.

??? example "Basic ArrayList Object"

    The variable `__array` holds the array to store the list items. Remember that the double underlines at the beginning will make the variable private or hidden.

    The variable `__capacity` holds the size of the array that stores the list items.

    The variable `__length` holds the amount of elements in the list at any point in time.

    ```mermaid
    classDiagram
        class ArrayList
        ArrayList : -__array [ ]
        ArrayList : -__capacity int
        ArrayList : -__length int
        ArrayList : +get(index) object
        ArrayList : +append(new_item) void
        ArrayList : +remove_at(index) void
        ArrayList : +is_empty() boolean
        ArrayList : +get_length() int
        ArrayList : +get_capacity() int
        ArrayList : +get_array() []
    ```

    The Python constructor creates the list's array and sets its initial capacity to the size given.

    - If the user does not give a `size`, the default value is used; 10 in the example below.
    - The value of the `__capacity` variable is set to the size that was used to create the array. This way, we can track the capacity and increase the array size when needed.
    - Finally, the `__length` variable is set to zero. Remember, the __length variable is the number of objects in the arraylist at any point in time.

    ```py
    def __init__(self, size=10):
        self.__array = [None] * size
        self.__capacity = size
        self.__length = 0
    ```