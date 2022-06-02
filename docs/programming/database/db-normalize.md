- _Primary Key_ = one or a combination of attributes that unquely identifies each record in a table. Should be: unique, minimal, not null, nonupdateable
    - Student ID
    - Employee ID
    - Vehicle VIN
- _Foreign Key_ = a field in a table that is a primary key in another table creating a relationship between the two tables
- _Entity integrity_ = describes a condition in which all rows within a table are **uniquely** identified by their primary key. The unique value requirement prohibits a null primary key value because null is not unique.
- _Referential integrity_ = describes a condition in which a foreign key value has amatch in the corresponding table or in which the foreign key value is null. It's impossible to assign a non-existant foreign key to a table. 

[DB Normalization](https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/)

**Database normalization** is a process used to organize a database into tables and columns. The main idea with this is that a table should be about a specific topic and only supporting topics included.

- By limiting a table to one purpose you reduce the number of duplicate data contained within your db. 
- DB normalization fixes modification anomalies
- There are 3 normal forms most db's adhere to using:
- These forms are progression, meaning to qualify for 3rd normal form a table must first satisfy 2nd and 1st normal forms. 
  - **First Normal Form** - The information is stored in a relational table with each column containing atomic values. There are no repeating values.
  - **Second Normal Form** - The table is in first normal form and all the columns depend on the table's primary key. 
  - **Third Normal Form** - The table is in second normal form and all of its columns are not transitively dependant on the primary key. 
