# `<Login> and <Auth>`
-  Can a component outside of a provider get its context?
   - Yes, if you get the **Invariant Violation** error it means your component is outside the connect() function. You can either wrap the root component in Provider, or pass a custom React context consumer to connect() options

## Vocab
- global state
  - It is only a way to pass props from a parent component to grandchild components without having to pass the props through all child components
- global context
  - provides a way to pass data through the component tree without having to pass props down manually at every level
- [provider](https://react-redux.js.org/api/provider)
  - The Provider component makes the [Redux store](https://redux.js.org/api/store) available to any nested components that have been wrapped in the **connect()** function

### Materials
- [what is role based access control?](https://digitalguardian.com/blog/what-role-based-access-control-rbac-examples-benefits-and-more)
- [react-cookies component](https://www.npmjs.com/package/react-cookies)
- [react-cookie library](https://www.npmjs.com/package/react-cookie)

 (../index.md)
