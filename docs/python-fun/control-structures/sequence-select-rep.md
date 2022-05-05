## Sequences

Sequences are ordered sets of objects indexed by non-negative integers which include the following objects:

- string
- list
- tuple
- range

Lists and tuples are sequences of arbitrary objects, where strings are sequences of characters.

String, tuple, and range objects are immutable, lists are mutable.

!!! note "All sequence types have a number of operations in common"
    - For immutable types, any operation will only return a value rather than actually change the value

??? example "Sequences Methods and Operations:"

    === "Methods"

        | Method                           	| Description                                                                                                               	|
        |----------------------------------	|---------------------------------------------------------------------------------------------------------------------------	|
        | len(s)                           	| Returns the number of elements in s.                                                                                      	|
        | min(s,[,default=obj, key=func])  	| Returns the minimum value in s (alphabetically for strings).                                                              	|
        | max(s,[,default=obj, key=func])  	| Returns the maximum value in s (alphabetically for strings).                                                              	|
        | sum(s,[,start=0])                	| Returns the sum of the elements (returns TypeError if s is not numeric).                                                  	|
        | all(s)                           	| Returns True if all elements in s are True (that is, not 0, False, or Null). any(s) Checks whether any item in s is True. 	|

    === "Operations"

        | Operation      	| Description                                                    	|
        |----------------	|----------------------------------------------------------------	|
        | s+r            	| Concatenates two sequences of the same type.                   	|
        | s*n            	| Makes n copies of s, where n is an integer.                    	|
        | v1,v2...,vn=s  	| Unpacks n variables from s to v1, v2, and so on.               	|
        | s[i]           	| Indexing returns the i element of s.                           	|
        | s[i:j:stride]  	| Slicing returns elements between i and j with optional stride. 	|
        | x in s         	| Returns True if the x element is in s.                         	|
        | x not in s     	| Returns True if the x element is not in s.                     	|

    === "Code Example"

        ```py
        Python 3.10.3 (v3.10.3:a342a49189, Mar 16 2022, 09:34:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
        Type "help", "copyright", "credits" or "license()" for more information.
        list()
        []
        list1 = [1, 2, 3, 4]
        list1.append(1)
        list1
        [1, 2, 3, 4, 1]
        list2 = list1 * 2
        list2
        [1, 2, 3, 4, 1, 1, 2, 3, 4, 1]
        min(list1)
        1
        max(list1)
        4
        list1.insert(0, 2)
        list1
        [2, 1, 2, 3, 4, 1]
        list1.reverse()
        list1
        [1, 4, 3, 2, 1, 2]
        list2 = [11, 12]
        list1.extend(list2)
        list1
        [1, 4, 3, 2, 1, 2, 11, 12]
        sum(list1)
        36
        len(list1)
        8
        list1.sort()
        list1
        [1, 1, 2, 2, 3, 4, 11, 12]
        list1.remove(12)
        list1
        [1, 1, 2, 2, 3, 4, 11]
        ```

## Selection

Selection statements are also known as _decision control statements_ or _branching statements_.

Selection statements allow a program to test several conditions and execute instructions based on which condition is true. Some of these conditional statements are listed here:

- Simple `if`
- `if-else`
- nested `if`
- `if-elif-else`

??? example "Control Flow with Examples"

    === "Simple if"

        _If statements_ are control flow statements that help to run particular code, but only when a certain condition is met or satisfied. Only has one condition to check

        ``` mermaid
        flowchart TD
          A[Start] --> B{Condition}
          B -->|If True| C[Execute Condition]
          C --> D[End]
          B ---->|If False| D[End]
        ```

        ```py
        n = 10
        if n % 2 == 0:
            print("n is an even number")
        ```

    === "if-else"

        _if-else statements_ evaluate the condition and will execute `if` the test condition is `True`, `else` if the condition is `False`, then a separate condition is executed instead.

        ``` mermaid
        flowchart TD
          A[Start] --> B{Expression Test}
          B -->|If True| C[Execute Condition]
          C --> E[End]
          B -->|If False| D[Execute Other Condition]
          D --> E[End]
        ```

        ```py
        n = 10
        if n % 2 == 0:
            print("n is an even number")
        else:
            print("n is an odd number")
        ```

    === "Nested if"

        _Nested if statements_ are if statements inside of another if statement.

        ``` mermaid
        flowchart TD
          A[Start] --> B{First Condition}
          B -- False --> C[Execute else statement]
          C --> B
          C ----> G[End]
          B -- If True --> D{Nested Second Condition}
          D -- If True --> E[Execute elif statements]
          E ----> G[End]
          D -- If False --> F[Execute else statement]
          F ----> G[End]
        ```

        ```py
        a = 5
        b = 10
        c = 15
        if a > b:
            if a > c:
                print("a value is big")
            else:
                print("c value is big")
        elif b > c:
            print("b value is big")
        else:
            print("c is big")
        ```

    === "if-elif-else"

        _if-elif-else statements_ are used to conditionally execute a statement or a block of statements. Typically when asserting if thing strictly equals value of something, if not, make another check, otherwise return this.

        ``` mermaid
        flowchart TD
          A[Start] --> B{Test If Expression}
          B -- True --> C[Execute If True]
          C ----> G[End]
          B -- If False --> D{Test Elif Expression}
          D -- If True --> E[Execute elif statements]
          E ----> G[End]
          D -- If False --> F[Execute else statement]
          F ----> G[End]
        ```

        ```py
        x = 15
        y = 12
        if x == y:
        print("Both are Equal")
        elif x > y:
            print("x is greater than y")
        else:
            print("x is smaller than y")
        ```

## Repetition

A **repetition statement** is used to repeat a group, or block, of code.

There's typically two statements in Python that can be used to instruct a program to loop back again until a condtion is met: the `for` and `while` loops.

??? example "Control flow and code examples for looping"

    === "for loops"

        A for loop is used to iterate over a sequence that is either a list, tuple, dictionary, or a set. Statements can execute once for each item in a list, tuple, or dictionary

        ``` mermaid
        flowchart TD
          A[For Index in List] --> B{Condition}
          B -- False --> D[End]
          B -- True --> C[Condition is true]
          C --> A
          C --> D[End]
        ```

        ```py
        lst = [1, 2, 3, 4, 5]
        for i in range(len(lst)):
            print(lst[i])
        ```
    === "while loops"

        While looops are used to execute a block of statements repeatedly until a given condition is satisfied. It will continue to loop as long as the expression is true, it will stop looping once the condition is false.

        ``` mermaid
        flowchart TD
          A[Start] --> B{Condition}
          B -- True --> C[Loop until False]
          C --> B
          B -- False --> D[Exit]
        ```

        ```py
        target = 5
        i = 0
        while i < target:
            print(i)
            i += 1
        ```