# Component Composition

1. [Can a parent component access the state of a child component?](https://linguinecode.com/post/get-child-component-state-from-parent-component)
   - Yes, but using a callback function on the child component
2. [What can be passed along in a prop variable?](https://medium.com/@cristi.nord/props-and-how-to-pass-props-to-components-in-react-part-1-b4c257381654)
   - Prop data can be passed along dynamically
3. How can a child component “know” the state of another component?
   - It would need to be a sibling component so the data can first be passed back to the parent and passed to the other child.

### Vocab

- [**_Component props_**]()
  - When React sees an element representing a user-defined component, it passes JSX attributes and children to this component as a single object called props
- [**_Component state_**](https://reactjs.org/docs/faq-state.html)
  - state differs from props in that props get passed _to_ the component (think params) whereas state is managed _within_ the component (similar to varialbes declared within a function)
- [**_Application state_**](https://medium.com/@devisha.singh/5-types-of-application-state-in-react-and-how-they-help-in-state-management-a6a76cb1479e)
  - There are 5 types of application state in react that handle state management.
    1. **Communication state** plays a crucial role in storing information in different states.
    1. **Data state** describes personal or business data like client details, project names, contacts, etc
    1. **Control state** refers to the state which the user has input into the app like form inputs, and selected items
    1. **Session state** contains information about the user of the app such as user id, permissions, passwords, or how app behavior based on user preferences.
    1. **Location state** is the UTF-8 display which appears in your URL bar. It's the "L" in URL, dawg.

#### Materials

[React Basics Recap](https://www.freecodecamp.org/news/these-are-the-concepts-you-should-know-in-react-js-after-you-learn-the-basics-ee1d2f4b8030/)
[props.children](https://codeburst.io/a-quick-intro-to-reacts-props-children-cb3d2fce4891)
[Composition vs inheritance](https://reactjs.org/docs/composition-vs-inheritance.html)
[React testing library](https://testing-library.com/docs/react-testing-library/example-intro/)
[React testing async utilities](https://testing-library.com/docs/dom-testing-library/api-async/)
[npm react-if component package](https://www.npmjs.com/package/react-if)

 (../index.md)
