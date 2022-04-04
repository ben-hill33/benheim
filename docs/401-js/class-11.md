# Authentication

- _Explain what a “Singleton” is (in Computer Science terms):_

  - A singleton is a class that allows only a single instance to be creatd and gives access to that created instance. it contains statis variables that can accomodate unique and private instances of itself.

- _Explain how the Singleton pattern can be used with Node modules, specifically with classes:_

  - A singleton represents a single instance of an object. Only one can be created, no matter how many times the object is instantiated. If there’s already an instance, the singleton will create a new one.
  - In the article below, the author shows a problem that is created where he created multiple instances of the Logger Class and got a problem in their console as a result. The author adds a class called Singleton class which carries a getInstance() method which allows us to instantiate one logger and then using the getInstance() method we can return that logger to any file that wants to use it.
  - He also noted that he needed to add the getInstance() method everywhere he had created a new instance of his Logger class. Which returns all of his instances in the CLI so he went back into logger and changed it to a single class.

  [Node.js Design Patterns - Singleton Pattern](https://medium.com/@maheshkumawat_83392/node-js-design-patterns-singleton-pattern-series-1-1e0ab71e3edf)

- _If you were tasked with building a middleware system like Express uses, what approach might you take to construct/operate it?:_

## Vocab

[_Router Middleware:_](https://blog.webdevsimplified.com/2019-12/express-middleware-in-depth/)

- Functions that execute some code before the controller action that sends the response and after the server gets the request from the client. aka code that executes in the middle of your request.
  Dynamic Module Loading:

_Singleton Pattern:_

- A singleton is a class that allows only a single instance to be creatd and gives access to that created instance. it contains statis variables that can accomodate unique and private instances of itself.

### Material

[Securing Passwords](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
[Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication)
[Intro to JWT](https://jwt.io/introduction/)
[OWASP auth cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
[bcrypt docs](https://www.npmjs.com/package/bcrypt)

[Table of Contents](../index.md)
