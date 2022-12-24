# SQL - Database language designed to interact w/ Relational Database Management systems to organize data into table w/ rows and columns.

# Database Management Systems: MySQL, PostgreSQL, SQLite.

'''
SQLite Types:
TEXT = 'City'
NUMERIC = bool, date
INTEGER = 0, 1, 2, -1, -2
REAL = 2.5, 3.6, 6.9
BLOB(Binary Large Object) = audio, video files, etc
'''

'''
MySQL Types:
CHAR(size) = used for fixed length of characters, if  length of characters are known ie. zipcode (The length can be any value from 0 to 255)

VARCHAR(size) = used for length that varies ie. name (The length can be specified as a value from 0 to 65,535)

SMALLINT = Allows whole numbers between -32,768 and 32,767. (Takes total numbers to be stored)

INT = Allows whole numbers between -2,147,483,648 and 2,147,483,647. (Takes total numbers to be stored)

BIGINT = Allows whole numbers between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807. (Takes total numbers to be stored)

FLOAT = A small (single-precision) floating-point number. Permissible values are -3.402823466E+38 to -1.175494351E-38, 0, and 1.175494351E-38 to 3.402823466E+38. (Takes total numbers to be stored / Number of digits after decimal)

DOUBLE = A normal-size (double-precision) floating-point number. Permissible values are -1.7976931348623157E+308 to -2.2250738585072014E-308, 0, and 2.2250738585072014E-308 to 1.7976931348623157E+308. (Takes total numbers to be stored / Number of digits after decimal)
'''

'''
Constraints: can be specified when the table is created with the CREATE TABLE statement, or after the table is created with the ALTER TABLE statement.

CHECK = Ensures that the values in a column satisfies a specific condition

DEFAULT = Sets a default value for a column if no value is specified

NOT NULL = Ensures that a column cannot have a NULL value

PRIMARY KEY = A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table

FOREIGN KEY = Prevents actions that would destroy links between tables

UNIQUE = Ensures that all values in a column are different

CREATE INDEX = Used to create and retrieve data from the database very quickly
'''

# Table 
'''
Syntax:
CREATE TABLE table_name (
  column1 datatype constraint,
  column2 datatype constraint,
  column3 datatype constraint,
  ....
);

CREATE TABLE flights (
  # Column: id
  # Type: INTEGER
  # Constraints: PRIMARY KEY - will be a unique way of accessing flight by id
  # Queue: AUTOINCREMENT - generates a new id when a new record/flight is added
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  # Column: origin
  # Type: TEXT
  # Constraints: NOT NULL - does not allow column to be empty
  origin TEXT NOT NULL,

  # Column: destination
  # Type: TEXT
  # Constraints: NOT NULL - does not allow column to be empty
  destination TEXT NOT NULL,

  # Column: duration
  # Type: INTEGER
  # Constraints: NOT NULL - does not allow column to be empty
  duration INTEGER NOT NULL
);
'''

# Add Data to Table
'''
INSERT INTO: statement is used to insert new records in a table. It is possible to write the INSERT INTO statement in two ways:


1. Specify both the column names and the values to be inserted:

SYNTAX:

  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
   
  INSERT INTO flights (origin, destination, duration)
  VALUES ('New York', 'London', 415)

  id | origin   | destination | duration
  1  | New York | London      | 415

2. If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the INSERT INTO syntax would be as follows:

SYNTAX:

  INSERT INTO table_name
  VALUES (value1, value2, value3, ...);
  
  INSERT INTO flights
  VALUES (origin, destination, duration);

  id | origin   | destination | duration
  1  | New York | London      | 415
'''

# Retrieve Data from Table: SQL Queries
'''
SELECT: statement is used to select data from a database. The data returned is stored in a result table, called the result-set.

SYNTAX:

  SELECT column1, column2, ...
  FROM table_name;  

  SELECT origin, duration
  FROM flights;

  Here, column1, column2, ... are the field names of the table you want to select data from.

If you want to select all the fields available in the table, use the following syntax:

SYNTAX:

  SELECT * FROM table_name;
  
  SELECT * FROM flights;

WHERE: clause is used to filter records. It is used to extract only those records that fulfill a specified condition.

WHERE SYNTAX: The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!

  SELECT column1, column2, ...
  FROM table_name
  WHERE condition;

  SELECT * FROM flights
  WHERE id = 3;

  id | origin     | destination
  3  | California | Japan

'''

# Accessing SQL Database:
'''
Create file: file_name.sql

Open Terminal/Run command: sqlite3 file_name.sql

  OUTPUT:
  SQLite version 3.40.0 2022-11-16 12:10:08
  Enter ".help" for usage hints.
  Connected to a transient in-memory database.
  Use ".open FILENAME" to reopen on a persistent database.

Create a Table:

  sqlite> CREATE TABLE flights (
    ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
    ...> origin TEXT NOT NULL,
    ...> destination TEXT NOT NULL,
    ...> duration INTEGER NOT NULL
    ...> );

Verify Tables: .tables

  sqlite> .tables

  OUTPUT:
  flights

Verify Table Data:

  sqlite> SELECT * FROM flights;

  OUTPUT:
  
Insert Data into Tables:

  sqlite> INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Florida', 360);

  Verify Table Data:

  sqlite> SELECT * FROM flights;

  OUTPUT:
  1|New York|Florida|360

  Additional Inserts:
  sqlite> INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
  sqlite> INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'New Jersey', 60);
  sqlite> INSERT INTO flights (origin, destination, duration) VALUES ('New Jersey', 'Virginia', 120);

  Verify Table Data:

  sqlite> SELECT * FROM flights;

  OUTPUT:
  1|New York|Florida|360
  2|New York|London|415
  3|New York|New Jersey|60
  4|New Jersey|Virginia|120

Organize Table Data: 

  sqlite> .mode columns
  sqlite> .headers yes

  Verify Table:

  sqlite> SELECT * FROM flights;

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Florida      360
  2   New York    London       415
  3   New York    New Jersey   60
  4   New Jersey  Virginia     120

Queries: Get flights WHERE origin = 'New York'

  sqlite> SELECT * FROM flights WHERE origin = 'New York';

  OUTPUT:
  id  origin    destination  duration
  --  --------  -----------  --------
  1   New York  Florida      360
  2   New York  London       415
  3   New York  New Jersey   60

'''

# Updating a Table:
'''
UPDATE: statement is used to modify the existing records in a table. Be careful when updating records in a table! Notice the WHERE clause in the UPDATE statement. The WHERE clause specifies which record(s) that should be updated. If you omit the WHERE clause, all records in the table will be updated!

SYNTAX:

  UPDATE table_name
  SET column1 = value1, column2 = value2, ...
  WHERE condition;

  UPDATE flights
  SET origin = 'New York', destination = 'Connecticut'
  WHERE id = 1;

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  

UPDATE Multiple Records:

SYNTAX:

  UPDATE table_name
  SET column1 = value1
  WHERE condition;

  UPDATE flights
  SET origin = 'California'
  WHERE origin = 'New York';

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  1   California  Connecticut  360
  2   California  London       415
  3   California  New Jersey   60
  4   New Jersey  Virginia     120

UPDATE WARNING!: Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!

SYNTAX:

  UPDATE table_name
  SET column1 = value1;

  UPDATE flights
  SET duration = 360;  

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  1   California  Connecticut  360
  2   California  London       360
  3   California  New Jersey   360
  4   New Jersey  Virginia     360
'''

# SQL Operators:
'''
AND, OR and NOT: The WHERE clause can be combined with AND, OR, and NOT operators.

The AND and OR operators are used to filter records based on more than one condition:

The AND operator displays a record if all the conditions separated by AND are TRUE.

AND Syntax:

  SELECT column1, column2, ...
  FROM table_name
  WHERE condition1 AND condition2 AND condition3;
  
  SELECT *
  FROM flights
  WHERE origin = 'New York' AND duration > 100;

  OUTPUT:
  id  origin    destination  duration
  --  --------  -----------  --------
  1   New York  Connecticut  360
  2   New York  London       360
  3   New York  New Jersey   360

The OR operator displays a record if any of the conditions separated by OR is TRUE.

OR Syntax:

  SELECT column1, column2, ...
  FROM table_name
  WHERE condition1 OR condition2 OR condition3;
  
  SELECT *
  FROM flights
  WHERE origin = 'New Jersey' OR duration < 100;

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  4   New Jersey  Virginia     360

The NOT operator displays a record if the condition(s) is NOT TRUE.

NOT Syntax:

  SELECT column1, column2, ...
  FROM table_name
  WHERE NOT condition;
  
  SELECT *
  FROM flights
  WHERE NOT destination = 'London';

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  3   New York    New Jersey   360
  4   New Jersey  Virginia     360

Combining AND, OR and NOT: You can also combine the AND, OR and NOT operators.

SYNTAX:

  SELECT *
  FROM table_name
  WHERE condition1 AND (condition2 OR condition3);
  
  SELECT *
  FROM flights
  WHERE origin = 'New York' AND (destination = 'London' OR destination = 'New Jersey');

  OUTPUT:
  id  origin    destination  duration
  --  --------  -----------  --------
  2   New York  London       360
  3   New York  New Jersey   360

  SELECT *
  FROM table_name
  WHERE NOT condition1 AND NOT condition2;
  
  SELECT *
  FROM flights
  WHERE NOT destination = 'London' AND NOT destination = 'New Jersey;

  OUTPUT:
  id  origin      destination  duration
  --  ----------  -----------  --------
  1   California  Connecticut  360
  4   New Jersey  Virginia     360

'''

# COUNT(), AVG(), and SUM() Functions:
'''
COUNT(): The COUNT() function returns the number of rows that matches a specified criterion.
Note: NULL values are not counted.

COUNT() Syntax:

  SELECT COUNT(column_name)
  FROM table_name
  WHERE condition;
  
  SELECT COUNT(id)
  FROM flights
  WHERE origin = 'New York';

  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  2   New York    London       630
  3   New York    New Jersey   60
  4   New Jersey  Virginia     360

  OUTPUT:
  3
  
  SELECT COUNT(column_name)
  FROM table_name
  
  SELECT COUNT(id)
  FROM flights

  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  2   New York    London       630
  3   New York    New Jersey   60
  4   New Jersey  Virginia     360

  OUTPUT:
  4

AVG(): The AVG() function returns the average value of a numeric column. 
Note: NULL values are not counted.

AVG() Syntax:

  SELECT AVG(column_name)
  FROM table_name
  WHERE condition;
  
  SELECT AVG(duration)
  FROM flights
  WHERE origin = 'New York';

  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  2   New York    London       630
  3   New York    New Jersey   60
  4   New Jersey  Virginia     360

  OUTPUT:
  350
  
  SELECT AVG(column_name)
  FROM table_name;
  
  SELECT AVG(duration)
  FROM flights;

  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  2   New York    London       630
  3   New York    New Jersey   60
  4   New Jersey  Virginia     360

  OUTPUT:
  352.5

SUM(): The SUM() function returns the total sum of a numeric column. 
Note: NULL values are not counted.

SUM() Syntax:

  SELECT SUM(column_name)
  FROM table_name
  WHERE condition;
  
  SELECT SUM(duration)
  FROM flights
  WHERE destination = 'Connecticut' AND destination = 'London';

  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  2   New York    London       630
  3   New York    New Jersey   60
  4   New Jersey  Virginia     360

  OUTPUT:
  990
  
  SELECT SUM(column_name)
  FROM table_name;
  
  SELECT SUM(duration)
  FROM flights;

  id  origin      destination  duration
  --  ----------  -----------  --------
  1   New York    Connecticut  360
  2   New York    London       630
  3   New York    New Jersey   60
  4   New Jersey  Virginia     360

  OUTPUT:
  1410
'''