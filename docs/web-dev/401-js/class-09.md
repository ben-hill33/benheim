# API Server

1. How does route prefixing work with an external routing module?

   - It works by naming your route handler function the same thing as your route prefix so it's invoked the same

2. When routing, what’s the difference between app.get('/data/:id') and app.get('/data/:name')?

   - The difference would be the data that your database is giving you for id and the json objects you get when getting name.

3. Explain how Express handles routing conflicts?

   - The parameters of the callback function are the request, object, the response object, the next middleware, the value of the parameter, and the name of the parameter, in that order. If they are out of order in your callback it will break.

4. What are the ways that a browser can send “data” or request variables to an HTTP server
   - The req object represents the HTTP request and has properties for the request query string, parameters, body, HTTP headers, and so on.

## Vocab

_Routing:_

- Routing refers to how an app's endpoints (URI's) respond to client requests. You define routing using methods of the Express app object that corresponds to HTTP methods i.e. app.get() to handle GET requests

_Route Prefixing:_

- Route prefixes are associated with routes by design in attribute routing. It is used to set a common prefix for an entire controller.

_Request “Body”:_

- Contains key-value pairs of data submitted in the request body. By default, it is undefined, and is populated when you use body-parsing middleware such as express.json() or express.urlencoded()

_Request “Query”:_

- This property is an object containing a property for each query string parameter in the route. When query parser is set to disabled, it is an empty object {}, otherwise it is the result of the configured query parser.

_Request “Params”:_

- This property is an object containing properties mapped to the named route "parameters". For example, if you have the route /user/:name, then the "name" property is available as req.params.name. This object defaults to {}.

### Material

- [express router.param() middleware](https://expressjs.com/en/4x/api.html#router.param)
- [mongoose middleware](https://mongoosejs.com/docs/middleware.html)
- [mongoose sub-documents](https://mongoosejs.com/docs/subdocs.html)
- [mongoose virtual joins](https://mongoosejs.com/docs/populate.html#populate-virtuals)

 (../index.md)
