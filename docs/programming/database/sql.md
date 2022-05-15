## :fontawesome-solid-database: What is SQL?

SQL - Structured Query Language

SQL is a language designed to allow both technical and non-technical users query, manipulate, and transform data from a relational database. Due to its simplicity, SQL databases provide safe and scalable storage for millions of websites and mobile apps.

- There are many SQL databases including:
- SQLite, MySQL, Postgres, Oracle and Microsoft SQL Servers. All of which support the common SQL language standard, but each implementation can differ in the additional features and storage types it supports.

??? note "Relational Databases"

    A relational database represents a collection of related (2-dimensional) tables. Each of the tables are similar to an Excel spreadsheet, with a fixed number of named columns (attributes) and any number of rows of data.

## DDL and DML

SQL has a number of commands in two general categories:

=== "Data Definition Language (DDL)" 

    _DDL_ consists of commands that are used to create new databases and tables as well as modify the structure of a database. DDL has more to do with the structure of the data, rather than the data itself.

    - Can add a new field to an existing table
    - Drop an existing table

    DDL Commands:

    - CREATE
    - DROP
    - ALTER
    - TRUNCATE

=== "Data Manipulation Language (DML)" 

    _DML_ consists of commands that work with the actual data in the database. 

    - Adds new records to a table
    - Modify existing records
    - Delete records
    - Retrieve records from one or more tables

    DML Commands

    - SELECT
    - INSERT
    - UPDATE
    - DELETE

## SQL Statements

??? info "DML Descriptions"

    === "SELECT"

        The SELECT statement is used for data retrieval.

        The simplest query you can use with `SELECT` is `*` or "all" rows in a table. 

        ```sql
        SELECT * FROM country;
        ```

        Best practice, however, is to query the Fields you're looking for. 

        ```sql
        SELECT Name, HeadOfState, Population FROM country;
        ```

        What if you don't know the names of the fields, or you're not wanting back every country on the planet that match the fields you're looking for? Click the `WHERE` link, and you'll have your answer.

        The `WHERE` clause can be used to filter out rows you don't need.

        ```sql
        SELECT * FROM country WHERE Continent = 'North America';
        ```

        The above query returns only countries in North America if you're querying the world database.

        !!! note "Single or double quotes can be used in SQL"

        The `LIKE` keyword and `%` wildcard can be used to include partial matches. A good example for the world db is if we were looking for countries that start with an "A":

        ```sql
        SELECT * FROM country WHERE Continent LIKE 'A%';
        ```

        If you want to sort the data that gets returned, `ORDER BY` can change the order of the rows ascending or descending by one or more fields. Query the world, and retrieve the GNP of all nations sorted from largest to smallest:

        ```sql
        SELECT Name, GNP FROM country ORDER BY GNP desc;
        ```

        Or what about:

        ```sql
        SELECT Name, SurfaceArea
        FROM country
        WHERE SurfaceArea <= 10000
        ORDER BY SurfaceArea;
        ```

        The `AS` keyword is used so that SQL doesn't return the formula. You can use the `AS` keyword to essentially rename anything you're using in your query.

        ```sql
        select Name, Population/SurfaceArea AS "Population per Square Mile"
        from country
        order by Population/SurfaceArea desc;
        ```

        Use the `DISTINCT` keyword to eliminate duplicate rows in results.

        ```sql
        SELECT DISTINCT Continent
        FROM country
        ORDER BY Continent;
        ```

        The above query would return seven continents rather than returning every instance of country in a continent.

        The `IN` keyword can be used with a list of items.

        ```sql
        SELECT *
        FROM country
        WHERE Continent IN ('North America','South America');
        ```

        The `BETWEEN` keyword indicates a range values

        ```sql
        SELECT *
        FROM country
        WHERE LifeExpectancy BETWEEN 50 AND 60
        ORDER BY LifeExpectancy;
        ```

        Null values, as it turns out, you can work with as long as the null values is using `IS NULL`

        ```sql
        SELECT *
        FROM country
        WHERE IndepYear IS NULL;
        ```

        We can therefore use `IS NOT NULL`

        ```sql
        SELECT *
        FROM country
        WHERE IndepYear IS NOT NULL;
        ```

        `AND` will only work if the words to the left and right of it match.

        ```sql
        SELECT *
        FROM country
        WHERE IndepYear IS NOT NULL AND Population BETWEEN 100000 AND 200000;
        ```

        `OR`, only one side has to be true.

        ```sql
        SELECT *
        FROM country
        WHERE IndepYear < 1900 OR Population > 200000;
        ```

        `NOT` is used to reverse the truth of an expression.

        ```sql
        SELECT *
        FROM country
        WHERE NOT Continent = 'Europe';
        ```

    === "INSERT"

        The `INSERT` statement adds new rows to the database and you can sort them other than the order they're in inside the database.

        ```sql
        INSERT INTO city
        VALUES (9000,'Pinecrest','USA','Florida',18657);
        ```
        ```sql
        INSERT INTO city (Name, District, CountryCode, ID)
        VALUES ('Miramar','Florida','USA',9001);
        ```

    === "UPDATE"

        Data living inside a database can and does age or get outdated. You can update outdated data using `UPDATE` which modifies the existing data.

        !!! danger "Use with caution!"
            Without the `WHERE` clause in the example query below, every record in the database would get updated.

        ```sql
        UPDATE country
        SET HeadOfState = 'Jane Smith'
        WHERE Code = 'USA';
        ```

    === "DELETE"

        You guess it! `DELETE` removes records from a table.

        ```sql
        DELETE
        FROM city
        WHERE ID = 9000;
        ```

        !!! warning "Don't forget the `WHERE` clause!"
            Unless you want to delete every record in the database

??? info "JOINS"

    There are two basic ways to join tables in a `SELECT` statement. Using the `FROM` or the `WHERE` clause. The goal is to link the primary and foreign keys from the tables needing to be joined respectively. 

    ```sql
    SELECT country.Name, LifeExpectancy, city.Name
    FROM country, city
    WHERE country.Code = city.CountryCode AND LifeExpectancy > 70;
    ```

    `country` and `city` create a link through dot notation for the `Name` field. The `WHERE` clause specifies the join.

    If we use the `FROM` clause, we can use the `JOIN` keyword.

    ```sql
    SELECT country.Name, LifeExpectancy, city.Name
    FROM country JOIN city on country.Code = city.CountryCode
    WHERE LifeExpectancy > 70;
    ```

    Notice that the join expression has been moved to the FROM clause, and the WHERE clause is used only to filter out the rows we don’t want.
    This example uses an _inner join_.

    === "NATURAL JOIN"

        _Natural Join_

          - Determines the common attributes by looking for attributes with identical names and compatible data types.
          - Selects only the rows with common values in the common attributes.
          - If there's no common attributes, returns the relational product of the two tables.

        ```sql
        SELECT CUS_CODE, CUS_LNAME, INV_NUMBER, INV_DATE
        FROM CUSTOMER NATURAL JOIN INVOICE;
        ```

        You're not limited to two tables

        !!! note
            While some DBMS include the `NATURAL JOIN` operator, it is generally discouraged in practice because it can be unclear to the programmer and to others performing maintenance on the code exactly which attribute or attributes the DBMS is using as the common attribute to perform the join.

    === "JOIN USING"

        Another way to express a join is through the `USING` keyword which returns only the rows with matching values in the column indicated in the `USING` clause which must exist in both tables.

        ```sql
        SELECT column-list 
        FROM table1 JOIN table2 USING (common-column)
        ```

        As with the `NATURAL JOIN` command, `JOIN USING` operand does not require table qualifiers and only returns one copy of the common attribute.

        !!! note
            Oracle and MySQL support the `JOIN USING` syntax, MS SQL Server and Access do not.

            - If `JOIN USING` is used in Oracle, then table qualifers can't be used with the common attribute in the query.
            - MySQL allows table qualifers on the common attribute anywhere except in the `USING` clause itself.

    === "JOIN ON"

        Another way to express a join when the tables _have no common attributes_ is to use the `JOIN ON` operand.

        - The query returns only the rows that meet the indicated join condition.
        - The join condition typically includes an equality comparison expression of two columns.
          - The columns may or may not share the same name, but obviously they must have comparable data types.

        ```sql
        SELECT colum-list
        FROM table1 JOIN table2 ON join-condition
        ```

        !!! note
            Best practice suggest that `JOIN ON` or `JOIN USING` should be used instead of `NATURAL JOIN` or other legacy-style joins. `JOIN USING` isn't widely supported among DBMS vendors and it requires that that the common attributes have exactly the same name in the tables being joined. When in doubt, just use `JOIN ON`.
