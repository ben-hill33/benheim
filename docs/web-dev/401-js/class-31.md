# Custom Hooks

1. What does a component’s lifecycle refer to?
   - There are three main phases which are mounting, updating, and unmounting
2. Why do you sometimes need to “wrap” functions in useCallback when called from within useEffect
   - So that you're utilizing that components props when it rerenders
3. Why are functional components preferred over class components?
   - For speed

### Vocab

- state hook
  - useState is a hook that lets you add react state to function components
- effect hook
  - lets you use side effects in function components. comparatively to lifecycle methods like componentDidMount, componentDidUpdate, and componentWillMount but it has all three of their functionality
- reducer hook
  - useReducer is usually preferable to useState when you have complex state logic that involves multiple sub-values or when the next state depends on the previous one. useReducer also lets you optimize performance for components that trigger deep updates because you can pass dispatch down instead of callbacks.

### Materials

#### Authoring

- [custom hooks - all you need to know](https://www.telerik.com/kendo-react-ui/react-hooks-guide/#toc-custom-react-hooks)
- [Hooks with async-await](https://dev.to/vinodchauhan7/react-hooks-with-async-await-1n9g)
- [useReducer Hook](https://reactjs.org/docs/hooks-reference.html#usereducer)
- [Building your own hooks](https://reactjs.org/docs/hooks-custom.html)

#### Hooks Lists/Collections

- [use hooks](https://usehooks.com/)
- [Hooks consortium repo](https://github.com/rehooks/awesome-react-hooks)
- [10 hooks to have in your toolbox](https://blog.bitsrc.io/10-react-custom-hooks-you-should-have-in-your-toolbox-aa27d3f5564d)

 (../index.md)
