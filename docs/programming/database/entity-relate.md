## :material-database: Storing Data

Before database management systems, programmers had to use file-based approaches to storing data. These files were typically processed one record at a time from top to bottom.

Because there was no program controlling access to these files, there was little security and was difficult for multiple programs or users to access the files simultaneously which could (and did) result in redundant, inconsistent, or missing data. 

## DBMS

To resolve the limitations of file processing, database management systems (DBMS) were created. 

**DBMS** is simply a program that handles all access and transactions to the database. User cases for the DBMS include, but is not limited to:

- Developers create applications that communicate with the DBMS and they can pass commands to add new records, update existing records, delete records, or retrieve records. (CRUD principle)
- Allows for secure access to the data while providing support for multiple users simultaneously. 
- Solves inconsistencies like data redundancy 
- Use more robust data models rather than flat files

### DBMS Functionality

The DBMS handles communication between the data and the application.