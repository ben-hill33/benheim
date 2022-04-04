# Routing

1. Do child components have direct access to props/state from the parent?
1. When a component “wraps” another component, how does the child component’s output get rendered?

```
<Main>
  <Content />
</Main>
```

3. Can a component, such as `<Content />`, which is a child also be used as a standalone component elsewhere in the application?
4. What trick can a parent use to share all props with it’s children

## Vocab

- props.children
- [composition](https://reactjs.org/docs/composition-vs-inheritance.html)
  - In react, composition is a natural pattern of the component model. It's how we build componenets from other components, of varying complexity and specialization through props.

### Further Reading:

- **_[browser router tutorial](https://blog.pshrmn.com/simple-react-router-v4-tutorial/)_**
- **_[browser router api docs](https://reactrouter.com/web/api)_**
- **_[react-if component](https://www.npmjs.com/package/react-if)_**
- **_[react testing library queries](https://testing-library.com/docs/dom-testing-library/api-queries/)_**
- **_[ARIA (Accessible Rich Internet Applications) roles](https://www.w3.org/TR/html-aria/)_**

[Table of Contents](../index.md)
