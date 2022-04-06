# Data in Microservices

Monolithic server approach: All code for an application is stored in one database

### What is a Microservice?
A Microservice contains all code required to make one feature work. A single microservice contains:
- Routing
- Middleware
- Business Logic
- Database access

The big challenge of microservices is data management between services. 
- With microservices, the way we store and access data is a little strange
  - Each service gets its own database (if it needs one)
  - Services will never, ever reach into another services database

The reason why is because we,
- want each service to run independently of other services
  - By having each service use its own DB, we reduce the risk of losing more than one feature if there's an issue with its DB.
  - If two services are using the same DB and that one DB crashes, we lose both services
- Database schema/structure might change unexpectedly 
  - If service A is getting user data from service B and B changes the key name for that object, A won't be able to get that data. 
- Some services might function more efficiently with different types of DB's (SQL vs NoSQL)

This is the business pattern for every enterprise that uses DB's as a service

### Big problems with Data

What if you're implementing a new feature that depends on data from other services? 
- If there's a db for user data
- If there's a db for ordering products
- Create a feature that tracks what a user has looked at
  - This would need user data and product data
  - You cannot use the db from the first two features
  - How do you get that data? 

#### Communication strategies
**Synchronous**
- Services communicate with each other using direct requests
  - Pros
    - Conceptually easy to understand
    - A new feature won't need a new database
  - Cons
    - Introduces a dependency between services
      - If any services go down, new service making direct requests will also have problems
    - If any inter-service request fails, the overall request fails
    - The entire request is only as fast as the slowest request
    - Can easily introduce webs of requests 
      - We may not actually know what each service is doing internally
      - That one service may be dependent on other services for its data
      - If any dependency fails, it slows down or breaks the program

**Asynchronous**
- Services communicate with each other using _events_
  - Having an event hub is a useful way to communicate between services
  - Each service emits an request event to the event hub 
    - Event hub takes that event and emits an event to a service that will have data for each type of request
    - Data that is being requested by Event hub is sent back to Event hub
    - Event hub emits event back to original service making request
  - Not conceptually easy to understand
  - Has all other cons of synchronous communication
- While other services are storing their own data to their own db's, they also emit an event to an Event hub that tells it what type of data was just saved
  - A new feature that wants data for user and product at the same time could have its own db with a collection for both of those things
  - When new user data emits event to Event hub
    - Event hub listens for new user data ID, emits user data 
      - new feature that stores user data and corresponding product data listens for new user data ID emitter and captures ID for its own DB that stores new user ID's
        - If there's no product history yet, create empty array ready to store it 
  - When that new user buys a product, product feature data emits event to Event hub
    - Event hub listens for new user product ID, emits user data
      - new feature that stores user data and corresponding product data listens for new user data ID emitter and captures ID for its own DB that stores new user product ID's
  - Pros
    - New service has zero dependencies on other services
      - Even if other services DB isn't functioning properly, it doesn't matter because those services emmitted an event that new service is storing in its own db
    - New service is extremely fast
  - Cons
    - Data duplication
      - While new service isn't capturing all data, it could still capture 
    - Paying for extra storage plus extra DB
      - This is arguably not even a con as hosting services charging like Asure, Google, and AWS charge around half a penny to store 1GB of data per month
        - The AWS API for example is about 1250 bytes of data for their products in JSON
        - 1250 bytes = about 6GB * $.115 * 100,000,000 = about $14.00
        - This is easily affordable
    - Harder to understand




 (../../index.md)
