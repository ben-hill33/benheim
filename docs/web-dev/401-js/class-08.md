# Express Routing

_True or false: The route handler is middleware?_

- True
  _In what ways can a middleware function end the process and send data to the browser?_

_At what point in the request lifecycle can you “inject” middleware?_
_What can cause express to error with “Request headers sent twice, cannot start a second response”_

### Vocab

- [_Middleware_](https://en.wikipedia.org/wiki/Middleware)
  - Middleware makes it easier for software developers to implement communication and input/output, so they can focus on the specific purpose of their application. It gained popularity in the 1980s as a solution to the problem of how to link newer applications to older legacy systems, although the term had been in use since 1968.
- [_Request Object_](https://expressjs.com/en/api.html#req)
  - The req object represents the HTTP request and has properties for the request query string, parameters, body, HTTP headers, and so on. In this documentation and by convention, the object is always referred to as req (and the HTTP response is res) but its actual name is determined by the parameters to the callback function in which you’re working.
- [_Response Object_](https://expressjs.com/en/api.html#res)
  - The res object represents the HTTP response that an Express app sends when it gets an HTTP request.
