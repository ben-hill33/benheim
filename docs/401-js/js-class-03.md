# Data Modeling & NoSQL Databases

## [Video](https://www.youtube.com/watch?v=ZS_kXvOeQ5Y)

## Related Articles

- [SQL vs NoSQL Database Differences Explained with few Example DB](https://www.thegeekstuff.com/2014/01/sql-vs-nosql-db/?utm_source=tuicool)
- [NoSQL Data Modeling Techniques](https://highlyscalable.wordpress.com/2012/03/01/nosql-data-modeling-techniques/)
- [Mongoose API](https://mongoosejs.com/docs/api.html#Model)

1. Why would a developer choose to make data models?

A data model helps design the database at the conceptual, physical and logical levels. Data Model structure helps to define the relational tables, primary and foreign keys and stored procedures. it provides a clear picture of the base data and can be used by database developers to create a physical database.

1. What purpose do CRUD operations serve?

In computer programming, create, read, update, and delete are the four basic functions of persistent storage. No app or database is complete without the ability to perform these basic operations.

1. What kind of database is Postgres? What kind of database is MongoDB?

- Postgres is an open source object-relational database
- Mongo is a cross-platform document-oriented database

1. What is Mongoose and why do we need it?

Mongoose is an object data modeling (ODM) library that provides a rigorous modeling environment for your data, enforcing structure as needed while still maintaining the flexibility that makes MongoDB powerful.

1. Define three related pieces of data in a possible application. An example for a store application might be Product, Category and Department. Describe the constraints and rules on each piece of data and how you would relate these pieces to each other. For example, each Product has a Category and belongs in a Department.

- Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. Some product use cases include:
  - Ad Tech:
    - User profile stores in RTB and ad targeting
    - User events, clickstreams, and impressions data store
    - Metadata stores for assets
    - Popular-item caches
  - Gaming:
    - Game states
    - Player data stores
    - Player session history data stores
    - Leaderboards
- Cosmos DB is Microsoft's globally distributed, multi-model database service. Some use cases include:
  - Gaming
  - Web and Mobile Apps
  - Retail and marketing
- Apache Cassandra is a free and open-source, distributed, wide column store, NoSQL db management system designed to handle large amounts of data across many commodity servers. Some use cases include:
  - Writes exceed reads by a large margin
  - Data is rarely updated and when updates are made they are idempotent
  - Read access is by a known primary key

## Cloud Databases

Alternatives to running Mongo locally:

[MLab](https://www.mlab.com/) - remotely hosted mongoDB systems. Easily setup a free database (or pay for more horsepower). Works great with Heroku

[Atlas](https://www.mongodb.com/cloud/atlas) - Cloud based, highly scalable Mongo DB

[DynamoDB](https://aws.amazon.com/dynamodb/) - AWS NoSQL Database. Very highly scalable. Also provides a ‘mongoose’-like ORM called ‘dynamoose’

[CosmosDB](https://cosmos.azure.com/) - The Microsoft Azure equivalent for Atlas and Dynamo

## Vocabulary

database:
A structered set of data held in a computer, especially one that is accessible in various ways. There are four different types of databases:

1. Text databases
1. Desktop db programs
1. Relational db management systems (RDMS)
1. NoSQL or object oriented db's

data model:
A data model is an abstract model that organizes elements of data and standardizes how they relate to one another and to the properties of real-world entities.

CRUD:
In computer programming, create, read, update, and delete are the four basic functions of persistent storage. No app or database is complete without the ability to perform these basic operations.

schema:
A database structure described in a formal language supported by db management system (DBMS). The term "schema" refers to the organization of data as a blueprint of how the db is constructed.

sanitize:
Data sanitization is the process of deliberately, permanently and irreversibly removing or destroying the data stored on a memory device to make it unrecoverable. A device that has been sanitized has no usable residual data, and even with the assistance of advanced forensic tools, the data will not ever be recovered.

Structured Query Language (SQL):
SQL statments are used to perform tasks such as update and retrieve data from a db.

Non SQL (NoSQL)
Non-relational db's provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational db's. They are inscreasingly used in big data and real-time web apps.

MongoDB:
One of hte most popular document based NoSQL database as it stores data in JSON like documents. It is non-relational database with dynamic schema. Written in C++

Mongoose
Mongoose is an object data modeling (ODM) library that provides a rigorous modeling environment for your data, enforcing structure as needed while still maintaining the flexibility that makes MongoDB powerful.

record:
In a db is an object that can contain one or more values.

document:
A document db is a type of non-relational db that is designed to store and query data as JSON-like documents. Make it easier for developers to store and query data in a db by using the same document-model format they use in their apps code.

Object Relation Mapping (ORM):
A programming technique for converting data between incompatible type systems using OOP languages. This creates a virtual db that can be used from within the programming language.

[Table of Contents](../index.md)
