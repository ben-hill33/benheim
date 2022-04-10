## :material-language-python: Modifying a List and Common List Operations

!!! note
    If you navigated to this page hoping to find the secrets of how to iterate through the length of a list from zero to the end of the universe.. You're in the wrong place!! Those secrets are safely tucked away. But if you're willing to click a link, click the one coming up in just a few words or less! :material-eye-refresh-outline:[Secrets of the universe and also list processing](lists.ipynb):material-eye-refresh-outline:

A list is **mutable** and is thus able to grow and shrink without the program having to replace the entire list with an updated copy. Such growing and shrinking capability is called in-place modification. The highlighted lines in the list below indicate ways to perform an in-place modification of the list:

??? example "Common List Operations"

    |           Operation          	|                                                            Description                                                           	|                           Example code                          	        |  Example output 	|
    |:----------------------------	|:--------------------------------------------------------------------------------------------------------------------------------:	|:---------------------------------------------------------------	        |:---------------:	|
    | my_list = [1, 2, 3]          	| Creates a list.                                                                                                                  	| my_list = [1, 2, 3]<br> print(my_list)                              	    | [1, 2, 3]       	|
    | list(iter)                   	| Creates a list.                                                                                                                  	| my_list = list('123')<br> print(my_list)                            	    | ['1', '2', '3'] 	|
    | my_list[index]               	| Get an element from a list.                                                                                                      	| my_list = [1, 2, 3]<br> print(my_list[1])                           	    | 2               	|
    | {==my_list[start:end]==}            	| {==Get a new list containing some of another list's elements.==}                                                                        	| {==my_list = [1, 2, 3]<br> print(my_list[1:3])  ==}                        	    | {==[2, 3]  ==}         	|
    | {==my_list1 + my_list2==}           	| {==Get a new list with elements of my_list2 added to end of my_list1.   ==}                                                             	| {==my_list = [1, 2] + [3] <br> print(my_list)==}                           	    | {==[1, 2, 3]==}        	|
    | {==my_list[i] = x ==}               	|{== Change the value of the ith element in-place. ==}                                                                                    	| {==my_list = [1, 2, 3]<br> my_list[2] = 9 <br> print(my_list)==}               	| {==[1, 2, 9]==}        	|
    | {==my_list[len(my_list):] = [x]==}  	| {==Add the elements in [x] to the end of my_list. The append(x) method (explained in another section) may be preferred for clarity.==}  	| {==my_list = [1, 2, 3] <br>my_list[len(my_list):] = [9]<br> print(my_list)==}  	| {==[1, 2, 3, 9]==}     	|
    | {==del my_list[i]==}                	| {==Delete an element from a list.    ==}                                                                                                	| {==my_list = [1, 2, 3]<br>del my_list[1]<br>print(my_list)  ==}              	    | {==[1, 3] ==}        	|

## :material-language-python: Common list methods

A list method can perform a useful operation on a list such as adding or removing elements, sorting, reversing, etc.

Some of the methods in the table below perform _in-place_ modifications of list elements -- you should be aware that a method that modifies a list in-place changes the underlying list object, and may affect the value of a variable that references the object.

??? example "Available List Methods"

    === "Adding Elements"
        
        | Method            | Description                           | Code                                        | Output        |
        | :---------------: | :-----------------------------------: | :-----------------------------------------: | :-----------: |
        | list.append(x)    | Add an item to the end of list.      	| my_list = [5, 8]<br>my_list.append(16)      | [5, 8, 16]    |
        | list.extend([x])  | Add all items in [x] to list.         | my_list = [5, 8]<br>my_list.extend([4, 12]) | [5, 8, 4, 12] |
        | list.insert(i, x) | Insert x into list before position i. | my_list = [5, 8]<br>my_list.insert(1, 1.7)  | [5, 1.7, 8]   |

    === "Removing Elements"

        | List Methods   	| Description                                   	| Code                                         	| Output              	|
        |----------------	|-----------------------------------------------	|----------------------------------------------	|---------------------	|
        | list.remove(x) 	| Remove first item from list with value x.     	| my_list = [5, 8, 14]<br>my_list.remove(8)    	| [5, 14]             	|
        | list.pop()     	| Remove and return last item in list.          	| my_list = [5, 8, 14]<br>val = my_list.pop()  	| [5, 8]<br>val is 14 	|
        | list.pop(i)    	| Remove and return item at position i in list. 	| my_list = [5, 8, 14]<br>val = my_list.pop(0) 	| [8, 14]<br>val is 5 	| 

    === "Modifying Elements"

        | Method         	| Description                            	| Code                                      	| Output     	|
        |----------------	|----------------------------------------	|-------------------------------------------	|------------	|
        | list.sort()    	| Sort the items of list in-place.       	| my_list = [14, 5, 8]<br>my_list.sort()   	    | [5, 8, 14] 	|
        | list.reverse()	| Reverse the elements of list in-place. 	| my_list = [14, 5, 8]<br>my_list.reverse() 	| [8, 5, 14] 	|

    === "Misc."

        | List Methods  	| Description                                      	| Code                                                  	| Output     	|
        |---------------	|--------------------------------------------------	|-------------------------------------------------------	|------------	|
        | list.index(x) 	| Return index of first item in list with value x. 	| my_list = [5, 8, 14]<br>print(my_list.index(14))      	| Prints "2" 	|
        | list.count(x) 	| Count the number of times value x is in list.    	| my_list = [5, 8, 5, 5, 14]<br>print(my_list.count(5)) 	| Prints "3" 	|

Good practice is to use list methods to add and delete list elements, rather than alternative add/delete approaches. 

Alternative approaches include syntax such as `my_list[len(my_list):] = [val]` to add to a list, or `del my_list[0]` to remove from a list. 

Generally, using a list method yields more readable code.

The `list.sort()` and `list.reverse()` methods rearrange a list element's ordering, performing in-place modification of the list.

The `list.index()` and `list.count()` return information about the list and do not modify the list.

??? question ":material-language-python:  Python's `enumerate()`: a Looping Primer :fontawesome-solid-person-walking-arrow-loop-left:"


### List Slicing

??? example "List Slicing Operations"

    === "Common Operations"

        |         Operation         	|                           Description                           	|                      Example code                      	|    Example output   	|
        |:-------------------------:	|:---------------------------------------------------------------:	|:------------------------------------------------------:	|:-------------------:	|
        | my_list[start:end]        	| Get a list from start to end (minus 1).                         	| my_list = [5, 10, 20]<br>print(my_list[0:2])           	| [5, 10]             	|
        | my_list[start:end:stride] 	| Get a list of every stride element from start to end (minus 1). 	| my_list = [5, 10, 20, 40, 80]<br>print(my_list[0:5:3]) 	| [5, 40]             	|
        | my_list[start:]           	| Get a list from start to end of the list.                       	| my_list = [5, 10, 20, 40, 80]<br>print(my_list[2:])    	| [20, 40, 80]        	|
        | my_list[:end]             	| Get a list from beginning of list to end (minus 1).             	| my_list = [5, 10, 20, 40, 80]<br>print(my_list[:4])    	| [5, 10, 20, 40]     	|
        | my_list[:]                	| Get a copy of the list.                                         	| my_list = [5, 10, 20, 40, 80]<br>print(my_list[:])     	| [5, 10, 20, 40, 80] 	|
