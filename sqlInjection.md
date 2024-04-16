
```bash
mysql -u root -p
```

**1. Show databases**

```sql
SHOW DATABASES;
```

**2. Create a new database**

```sql
CREATE DATABASE my_new_database;
```

**3. Use the database**

```sql
USE my_new_database;
```

**4. Show tables inside the database**

```sql
SHOW TABLES; 
```

**5. Create a new table with dummy values**

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (id, name, password)
VALUES 
    (1, 'John Doe', 'securepassword1'),
    (2, 'Jane Smith', 'mypassword123'),
    (3, 'Alex Johnson', 'strongpassword');
```

**Explanation**

* **DDL (Data Definition Language)**
    * `CREATE DATABASE` - Creates a new database
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

```sql
SELECT * FROM users where id = 2 or 1 = 1;
```