## :material-language-python: Dictionaries

A dictionary is another type of container object that is different from sequences like strings, tuples, and lists. 

Dictionaries contain references to objects as_ key-value pairs_ – each key in the dictionary is associated with a value, much like each word in an English language dictionary is associated with a definition. Unlike sequences, the elements of a dictionary do not have a relative ordering of positions. The `dict` type implements a dictionary in Python.

There's a few common approaches to creating a `dict`:

- The first approach wraps braces { } around key-value pairs of literals and/or variables:
  -  `{'Jose': 'A+', 'Gino': 'C-'}` creates a dictionary with two keys `'Jose'` and `'Gino'`that are associated with the grades` 'A+'` and` 'C-'` respectively.
- The second approach uses dictionary comprehension, _which evaluates an object to create a new dictionary_, similar to how list comprehension creates a new list:

``` python
words = ['be', 'is', 'are'] 
word_length = {word: len(word) for word in words} 
print(word_length) 

# Output
{'be': 2, 'is': 2, 'are': 3}
```

- Other approaches use the `dict()` built-in function, using either keyword arguments to specify the key-value pairs or by specifying a list of tuple-pairs. The following creates equivalent dictionaries:
dict(Bobby='805-555-2232', Johnny='951-555-0055')
dict([('Bobby', '805-555-2232'), ('Johnny', '951-555-0055')])

In practice, a programmer first creates a dictionary and then adds entries, perhaps by reading user-input or text from a file.

_Dictionaries are mutable_, thus entries can be added, modified, or removed in-place. The table below shows some common dict operations.

??? example "Common `dict` operations"

    |       Operation      	|                                  Description                                 	|         Example code         	|
    |:--------------------:	|:----------------------------------------------------------------------------:	|:----------------------------:	|
    | my_dict[key]         	| Indexing operation – retrieves the value associated with key.                	| jose_grade = my_dict['Jose'] 	|
    | my_dict[key] = value 	| Adds an entry if the entry does not exist, else modifies the existing entry. 	| my_dict['Jose'] = 'B+'       	|
    | del my_dict[key]     	| Deletes the key entry from a dict.                                           	| del my_dict['Jose']          	|
    | key in my_dict       	| Tests for existence of key in my_dict.                                       	| if 'Jose' in my_dict: # ...  	|

## Dictionary Methods

A dictionary method is a function provided by the dictionary type (dict) that operates on a specific dictionary object. 

Dictionary methods can perform some useful operations, such as adding or removing elements, obtaining all the keys or values in the dictionary, merging dictionaries, etc.

??? example "Dictionary methods"
    |     Dictionary method     	|                                                                  Description                                                                  	|                                                 Code example                                                 	|                Output                	|
    |:-------------------------:	|:---------------------------------------------------------------------------------------------------------------------------------------------:	|:------------------------------------------------------------------------------------------------------------:	|:------------------------------------:	|
    | my_dict.clear()           	| Removes all items from the dictionary.                                                                                                        	| my_dict = {'Ahmad': 1, 'Jane': 42}<br>my_dict.clear()<br>print(my_dict)                                      	| {}                                   	|
    | my_dict.get(key, default) 	| Reads the value of the key entry from the dictionary. If the key does not exist in the dictionary, then returns default.                      	| my_dict = {'Ahmad': 1, 'Jane': 42}<br>print(my_dict.get('Jane', 'N/A'))<br>print(my_dict.get('Chad', 'N/A')) 	| 42 N/A                               	|
    | my_dict1.update(my_dict2) 	| Merges dictionary my_dict1 with another dictionary my_dict2. Existing entries in my_dict1 are overwritten if the same keys exist in my_dict2. 	| my_dict = {'Ahmad': 1, 'Jane': 42}<br>my_dict.update({'John': 50})<br>print(my_dict)                         	| {'Ahmad': 1, 'Jane': 42, 'John': 50} 	|
    | my_dict.pop(key, default) 	| Removes and returns the key value from the dictionary. If key does not exist, then default is returned.                                       	| my_dict = {'Ahmad': 1, 'Jane': 42}<br>val = my_dict.pop('Ahmad')<br>print(my_dict)                           	| {'Jane': 42}                         	|

??? info "Resources"

    [Dictionaries in Python](https://realpython.com/python-dicts/)
