# Back end performance

## CDNs

Content delivery network

The reason CDN's are used is because of _latency_. Which is the delay of a hosting server to a client request due to physical space. 

For example, if I'm making a request in Seattle, and the hosting server is in India, a CDN service will have that request data that was _cached_ from the hosting server and makes the response time much faster.

## Gzip

Is a package you can use with express as middleware in order to compress file sizes that will automatically decrease file sizes. 

_Brotli_, by Google, actually does the same thing faster, but it's a newer service. Which means companies are likely going to be gradually switching to it as it will increase performance. Browsers are currently trying to implement brotli over gzip.

## Database Scaling

THere are 6 main ways that a database can scale:
1. Identify inefficient queries
    - Only make requests that are really needed
    - Storage is the slowest piece
2. Increase memory
3. Vertical scaling (Redis, Memcached)
4. Sharding
     - Difficult to do
     - When a database gets too big you can partition the data into separate pieces
5. More databases
6. Database type

## Caching

Is the process of storing some data in a cache so data can be served faster.

CPU's are built with on chip memory called registers. They're the closest and smallest memory storage we have access to. The fastest method of storage

RAM (random access memory) 

HDD (hard disk drives) or SDD (solid state drive) will remember data long term over CPU's and RAM that are stored in memory.

Before you do any sort of database scaling, you want to see if you can cache your data. 

The browser for instance caches data in 
- Cache Storage, 
- Session Storage, and 
- Local Storage

Browsers do this automatically, but we can control it. A problem is that if changes are made at development, the cache storage won't remember.

A solution for this is called _cache busting_. 

Cache-control
Etag

Serve static files where you can serve the filename and set a max age for the page to cache that data on disk

### Further reading on Caching:
- [Caching Everywhere](https://www.freecodecamp.org/news/the-hidden-components-of-web-caching-970854fe2c49/)
- [Cache headers (prevent unnecessary network requests)](https://web.dev/http-cache/)
- [Caching and Performance](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers)

## Load Balancing

A way to balance multiple requests at the same time and distribute them. 

Third party servers are usually the way companies will go that don't have developers. Which in turn use Apache and Nginx, probably. 

When your database gets too big, you can have multiple servers to handle more and more requests. What Apache and Nginx do is, listen for the request, and determine which one of your servers has the lightest request load ie, which server is busier. Then it will send the request to the server that has the lightest load. 

They can also automatically cache data for you as you're making the request. Ideally, you want to use a load balancer only when your servers are struggling from traffic. If you don't have that many users, probably a wasted resource. 

 (../index.md)
