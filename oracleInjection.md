```sql
CREATE TABLE users (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(50),
    password VARCHAR2(50)
);

INSERT INTO users (id, name, password)
VALUES 
    (1, 'John Doe', 'securepassword1');

INSERT INTO users (id, name, password)
VALUES 
    (2, 'Jane Smith', 'mypassword123');

INSERT INTO users (id, name, password)
VALUES 
    (3, 'Alex Johnson', 'strongpassword');
```

**Explanation**

* **DDL (Data Definition Language)**
    * `CREATE USER` - Creates a new user (schema) in Oracle
    * `CREATE TABLE` -  Creates a new table with specified columns and data types 
* **DML (Data Manipulation Language)** 
    * `INSERT INTO` - Inserts new rows of data into the table.

**Basic SQL Commands**

* **SELECT** - Retrieves data from tables
   ```sql
   SELECT * FROM users; -- Get all columns and rows
   SELECT name, password FROM users; -- Get specific columns
   ```
* **WHERE** - Filters data based on conditions
   ```sql
   SELECT * FROM users WHERE id = 2; 
   ```
* **UPDATE** - Modifies existing data in tables
    ```sql
    UPDATE users SET password = 'newstrongpassword' WHERE id = 1;
    ```
* **DELETE** - Removes rows from a table
    ```sql
    DELETE FROM users WHERE name = 'Alex Johnson';
    ```

**SQL Injection**

Oracle SQL injection is similar to MySQL. Here’s an example:

```sql
SELECT * FROM users WHERE id = 2 OR 1 = 1;
```