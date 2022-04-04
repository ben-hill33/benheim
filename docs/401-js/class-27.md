# Props and State

1. Does a deployed React application require a server?
   - If it's deployed, it will have a server, yes
2. [Why do we prefer to test a React application at the behavior rather than the unit level?](https://reactjs.org/docs/testing.html)
   - Behavior describes how the code is working not just through unit testing but how the solution was derived. Unit tests just test against the workability of a particular function or method.
3. [What does npm run build do?](https://docs.npmjs.com/cli/v6/commands/npm-build)
   - npm run build does nothing unless you specify what "build" does in your package.json file. It lets you perform any necessary building/prep tasks for your project, prior to it being used in another project.
4. [Describe the actual composition / architecture of a React application](https://skillcrush.com/blog/what-is-react-js/)

### Vocab

- [Behavior-driven Development(BDD)](https://en.wikipedia.org/wiki/Behavior-driven_development)
  - BDD is an Agile software development proces that encourages collaboration among developers, QA and non-technical or business participants on a software project. It enourages teams to use conversation and concrete examples to formalize a shared understanding of how the application should behave.
  - BDD emerged from TDD.
  - BDD combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software development and management teams with shared tools and a shared process to collaborate on an app
  - BDD is largely facilitated through the use of a simple domain-specific language (DSL) using natural-language constructs (English like sentences) that can express the behavior and expected outcomes.
- [Acceptance Tests](<https://www.agilealliance.org/glossary/acceptance/#q=~(infinite~false~filters~(postType~(~'page~'post~'aa_book~'aa_event_session~'aa_experience_report~'aa_glossary~'aa_research_paper~'aa_video)~tags~(~'acceptance*20test))~searchTerm~'~sort~false~sortDirection~'asc~page~1)>)
  - are formal descriptions of the behavior of a software product, generally expressed as an example or a usage scenario.
    - similar to a unit test, an acceptance test generally has a binary result, pass or fail. A failure suggest, though does not prove, the presense of a defect in the product.
- [Mounting](<https://en.wikipedia.org/wiki/Mount_(computing)>)
  - is a process by which the operating system makes files and directories on a storage device (hard-drive, CD, or network share) available for users to access via the computer's file system.
  - in general, mountin comprises the OS acquiring access to the storage medium; recognizing, reading, and processing file system structure and metadata on it before registering them to the virtual file system (VFS) component.
- [Build](<https://www.agilealliance.org/glossary/automated-build/#q=~(infinite~false~filters~(postType~(~'page~'post~'aa_book~'aa_event_session~'aa_glossary~'aa_organizations~'aa_research_paper~'aa_video)~tags~(~'automated*20build))~searchTerm~'~sort~false~sortDirection~'asc~page~1)>)
  - refers to the process that converts files and other assets under the developers' responsibility into a software product in its final or consumable form.
  - The build may include:
    - compiling source files
    - packaging compiled files into compressed formats (such as jar, zip)
    - producing installers
    - creating or updating of database schema or data
  - The build is automated when these steps are repeatable, require no direct human intervention, and can be performed at any time with no information other than what is stored in the source code control repository.
- [setState](https://css-tricks.com/understanding-react-setstate/)
  - Is the only legitimate way to update state after the initial state setup.
  - When triggered, setState triggers a process that React calls _reconciliation_, which is the process React uses to update the DOM.
  - When a request triggers setState, React creates a new tree containing the reactive elements in the component along with the updated state.
    - This tree is used to figure out how the Search component's UI should change in response to the state change by compairing it with the elements of the previous tree.
    - React knows which changes to implement and will only update the parts of the DOM where necessary.
  - The rule of of thumb is to never mutate state directly. Always use a setState() to change the state.

#### Materials

- [Handling Events](https://reactjs.org/docs/handling-events.html)
- [Forms](https://reactjs.org/docs/forms.html)
- [State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)
- [Components and Props](https://reactjs.org/docs/components-and-props.html)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Beginners guide to testing React Apps (updated 2020)](https://thomlom.dev/beginner-guide-testing-react-apps/)
- [React Roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques#Roles)
- [Testing Recipes](https://reactjs.org/docs/testing-recipes.html)
- [Testing Environments](https://reactjs.org/docs/testing-environments.html)

[Table of Contents](../index.md)
