# [Python Scope](https://realpython.com/python-scope-legb-rule/)

- ### Global (module) scope
  - is the top most scope in a python program, script, or module.
  - Internally, Python turns your program's main script your program's main script into a module called __main__ to hold the main program's execution
    - the namespace of this module is the main global scope of your program
  - Whenever you run a python program, the interpreter executes the code in the module or script that serves as an entry point to your program. 
  - To inspect names within your global scope, you can use the dir() module
    - calling it without arguments, you'll get a list of names that live in your current global scope. 
    - you can add to the list if you assign a new name (example) at the top level of the module
  - There's only one global python scope per program execution. 
    - This scope remains in existence until the program terminates and all its names are forgotten. 
  - Whenever you assign a value to a name in python, one of two things can happen:
    - you create a new name
    - you update an existing name
    - The behavior will depend on the python scope in which you're assigning the name. If you try to assign a value to a global name inside a function, you'll be creating that name in the function's local scope, shadowing or overriding the global name. This means that you won't be able to change most variables that have been dfined outside the function from within the function
  - This will raise an UnboundLocalError: local variable referenced before assignment
  - Good programming practice recommends using local names rather than global names
    - **Write** self contained functions that rely on local nammes rather than global ones
    - **Try** to use unique object names, no matter what scope you're in
    - **Avoid** global name modifications thoughout your programs
    - **Avoid** cross-module name modifications
    - **Use** global names as constants that don't change during your program's execution

### Modifying Python Scope Behavior
The above are general rules by default, but there are ways to modify this standard behavior. Python provides two keywords that allow you to modify the content of global and nonlocal names:
  - global
  - nonlocal
### The global statement
The global statement is a method to modify the behavior of global names within functions.
- The statement consists of the **global** keyword followed by one or more names separated by commas:
```
counter = 0
def local_counter():
  global counter
  counter =  counter + 1

local_counter()
counter
```
### The nonlocal statement
Similarly to global names, nonlocal names can be accessed from inner functions, but not assigned or updated. If you want to modify them use the **nonlocal** statement
- With a nonlocal statement, you can define a list of names that are going to be treated as nonlocal 
- Unlike **global**, you can't use **nonlocal** outside of a nested or enclosed function. 
  - More precisely, you can't use a nonlocal statement in either the global or local scope
  - you can modify using nonlocal in a nested function that's still within the local scope if the first function. 
    - in the nested function, you use the **nonlocal** keyword and can modify the variable there, then call the first function it's nested in 

### Lecture
Automated user acceptance tests are going to be primary goal for this lab

Tests will be written using flo.py - what is that?

Testing of game logic will be simulated from the users point of view. 
- With user acceptance testing, we have to modify the way we think about the test
- how do we test 
- make sure you're importing "quitter.sim.path"

Tab times 
- 8:41: start
- 

 (../index.md)
