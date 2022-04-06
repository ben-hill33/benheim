# Classes, Inheritance, Functional Programming

- Name 3 advantages to Test Driven Development

  - Better program design and higher code quality
  - Detailed project documentation
  - TDD reduces the time required for project development

- In what case would you need to use beforeEach() or afterEach() in a test suite?

  - they're both used when you need to work that needs to be tested repeatedly.
  - can handle async code in the same ways that tests can handle acync code
  - they can either take a **done** parameter or return a promise.

- What is one downside of Test Driven Development

  - it necessitates a lot of time and effort up front, which can make development feel slow to begin
  - Focusing on the simplest design now and not thinking ahead can mean major requirements
  - It's difficult to write good tests that cover the essentials and avoid the superfluous

- What’s the primary difference between ES6 Classes and Constructor/Prototype Classes?
  - The most important difference between class- and prototype-based inheritance is that a class defines a **type** which can be instantiated at runtime, whereas a prototype is itself an object instance
- Name a use case for a static method
  - the static keyword defines a static method for a class. Static methods aren't called on instances of the class. Instead, they're called on the class itself. Often utility functions, such as functions to create or clone objects.
- Write an example of a Higher Order function and describe the use case it solves
  - The following function's use case is to create another function
    `function greaterThan(n) { return m => m > n; } let greaterThan10 = greaterThan(10); console.log(greaterThan10(11)); // → true`

## Vocabulary

functional programming:

- Function programming (FP) is the process of building software by composing pure functions, avoiding shared state, mutable data, and side-effects.
- is declarative rather than imperative, and application state flows through pure functions

pure function:

- a function which: given the same input, will always return the same output. Produces no side effects.

higher-order function:

- a function that can take another function as an argument, or that returns a function as a result

immutable state:

- immutable (means unchanging) objects is an object whose state can't be modified after its been created.

object:

- a collection of properties with key value pair

object-oriented programming (OOP):

- the basic idea of OOP is that we use objects to model real world things that we want to represent inside our programs, and/or provide a simple way to access functionality that would otherwise be hard or impossible to make use of.

class:

- a class is an extensible program-code-template for creating objects, providing values for state and implementations of behavior (functions or methods)

prototype:
Each object in JS has a private property which holds a link to another object called its prototype. The prototype object has a prototype of its own, and so on until an object is reached with **null** as its prototype. By definition null has no prototype and acts as the final link in the prototype chain.

super:

- is a keyword that refers to the parent class. it's used to call the constructor of the parent class and to access the parents properties and methods.

inheritance:

- ancestors and descendants

constructor:

- a function that creates an instance of a class which is typically called an object. in JS, a constructor gets called when you declare an object using the **new** keyword. The purpose of a constructor is to create an object and set values if there are any object properties present.

instance:

- instance means a reference to an object created by new or the equivalent. What's speical about JS, and other scripting languages, is that an "instance" is just a regular object; it's not what it is, but how it's made that is different.

context:

- what the value of "this" is.

this:

- The value of this is determined by how a function is called (runtime binding). It can't be set by assignment during execution, and it may be different each time the function is called.
- in the **global execution context**(outside of any function), this refers to the global object whether in strict mode or not
- **inside a function,** the value of this depends on how the function is called. In strict mode, the value of this is not set when entering an execution context: to set the value of this to a particular value when calling a function, use **call()**, or **apply()**
- in **classes** this is a regular object. All non-static methods within the class are added to the prototype of this

Test Driven Development (TDD):

- is a programming methodology with which one can tackle design, implementation, and testing of units of code, and to some extent the expected functionality of a program.

[Jest:](https://jestjs.io/)

- Is a JS testing framework designed to ensure correctness of any JS codebase. It allows you to write tests with an approachable, familiar and feature-rich API that gives you results quickly.

Continuous Integration (CI):

- is a development practice where devs integrate code into a shared repository frequently, prefereably several times a day. Each integration can then be verified by an automated build and automated tests.

unit test:

- Unit testing is a level of software testing where individual units/ components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable party of any software. It usually has one or a few inputs and usually a single output.

 (../index.md)
