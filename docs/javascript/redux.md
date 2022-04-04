# Redux

Why use redux? 

Firstly, redux is a tool used to manage state in React. When we have a ton of hooks and props all pointing back to one another for our components, it can get pretty confusing and make debugging nightmare.

Redux changes the state of your React program and gives you one prop object.
- It's good for managing large state
  - Use redux library when the program gets bigger and bigger and more complicated
- Useful for sharing data between containers
  - When projects get too large and need to start sharing state between components, redux makes it much easier
- Predictable state management using the 3 principles
  - Single source of truth
    - One state object management
  - State is read only
    - Immutability, never gets modified
  - Changes using pure functions
    - Receives input with predictable output

## Vocab
- **Action**
  - Something a user does
    - Clicks on something
- **Reducer**
  - is a function that takes an input, and creates an output called a store
- **Store**
  - The entire state of the app
- **Make changes**
  - React makes changes to the view layer based on the previous three, action, reduce, and store

Redux takes all the complications of state with the above vocab and makes it flow easier which is commonly referred to as the _flux pattern_

**Flux Pattern** inspired the need for redux
- Action ->
- Dispatcher ->
- Store ->
- View ->

This flux pattern replaces the MVC pattern, respectively. The problem was the Action would flow into Controller which would flow into a disaster of things pointing in all sorts of different  ways.

At the end of the day. Redux replaces `this.state` with one caveat. You could technically have redux state with React state 

[Table of Contents](../index.md)
