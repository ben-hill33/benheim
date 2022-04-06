# Node Ecosystem, TDD, CI/CD

1. **What is the difference between a module and a package?** A package must contain a package.json file in order to be published to the npm registry. Modules are not required to have a package.json file, not all modules are packages but just a file that exists within node_modules. Modules are the thing that is loaded from a file.

1. **What does the node package manager do?** npm is used to:

- Adapt packages of code for your apps
- Download standalone tools you can use right away.
- Manage multiple versions of code and code dependencies.
- Update apps easily when underlying code is updated.
- Discover muliple ways to solve the same puzzle.

npm consists of three distinct components:

- the website
- the Command Line Interface
- the registry
  For more see [npm docs](https://docs.npmjs.com/about-npm/)

## Vocabulary

- **ecosystem** - "A collection of software projects, which are developed and co-evolve in the same environment." The environment can be organizational, social, or technical. The ecosystem metaphor is used in order to denote an analysis which takes into account multiple software systems. (Cited from Wikipedia)
- **Node.js** - Is a platform built on Chrome's JS runtime for easily building fast and scalable network apps. It uses an event-driven, non-blocking Input/Output model that makes it lightweight and efficient, perfect for data-intensive real-time apps that run across distributed devices.
- **V8 Engine** - V8 is Google's open source, high-performance JS and WebAssembly engine... written in C++ lol. Used in Chrome and Node.js; it implements ECMAScript on windows 7 or later, macOS 10.12 or later. It compiles and executes JS source code, handles memory allocation for objects, and garbage collects objects it no longer needs. It provides data types, operators, objects, and functions specified in the ECMA standard. [v8 docs](https://v8.dev/docs)
- **module** - A module is any file or directory in the **node_modules** directory that can be loaded by the Node.js **require()** function. Modules are not required to have a package.json file.
- **package** - The npm registry contains packages, a package is a file or directory that is described by a package.json file. They can be scoped or unscoped to a user or Org, and scoped packages can be private or public. Must have package.json file.
- **node package manager (npm)** - The world's largest software registry. Open source devs from every continent use npm to share and borrow packages, and many organizations use npm to manage private development as well.
- **server** - A piece of hardware or software that provides functionality for other programs or devices called "clients". The server "serves" the "clients" request, typically by requesting information from a database, and then posts it back to the client.
- **environment** - Typically it means running programs on a compatible operating system or language specific functionality. A good example for node is when we use "express" we create an environment in our editor for use of that module when we say that app = express.
- **interpreter** - A computer program that directly executes instructions written in a programming or scripting language, without requiring them previously to have been compiled into a machine language program. (wiki)
- **compiler** - Is a computer program that translates computer code written in one programming language into another language. (wiki)

 (../index.md)
