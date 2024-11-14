
import sqlite3
import pandas as pd

def main():

    ### Relational Databases & Database, Table, Rows and Columns
    # . Access to data by multiple simultaneous users
    # • Protection from corruption by those users
    # • Efficient methods to store and retrieve the data
    # • Data defined by schemas and limited by constraints
    # • Joins to find relationships across diverse types of data
    # • A declarative (rather than imperative) query language: SQL (Structured Query Language)

    # These are called relational because they show relationships among different kinds of data in the form of tables
    # A table is a grid of rows and columns, similar to a spreadsheet. To create a table, name it and
    # specify the order, names, and types of its columns. Each row has the same columns, although a column
    # may be defined to allow missing data (called nulls).

    ###  Primary Key & Indexing
    # A column or group of columns is usually the table’s primary key; its values must be
    # unique in the table. This prevents adding the same data to the table more than once.
    # This key is indexed for fast lookups during queries. An index works a little like a book index,
    # making it fast to find a particular row.

    # Each table lives within a parent database, like a file within a directory. Two levels of
    # hierarchy help keep things organized a little better.

    ### Secondary Index
    # If you want to find rows by some non-key column value, define a secondary index on
    # that column. Otherwise, the database server must perform a table scan—a brute-force
    # search of every row for matching column values.

    ### Foreign Keys
    # Tables can be related to each other with foreign keys, and column values can be con‐
    # strained to these keys.

    ### SQL
    # SQL is not an API or a protocol, but a declarative language: you say what you want
    # rather than how to do it. It’s the universal language of relational databases.

    # Two main categories of SQL - Data Definition Language(DDL) and Data Manipulation Language(DML)
    # OperationSQL                             patternSQL                           example
    # Create a database                   CREATE DATABASE dbname                CREATE DATABASE d
    # Select current database             USE dbname                            USE d
    # Delete a database and its tables    DROP DATABASE dbname                  DROP DATABASE d
    # Create a table                      CREATE TABLE tbname ( coldefs )       CREATE TABLE t (id INT, count INT)
    # Delete a table                      DROP TABLE tbname                     DROP TABLE t
    # Remove all rows from a table        TRUNCATE TABLE tbname                 TRUNCATE TABLE t

    # The main DML operations of a relational database are often known by the acronym CRUD:
    # • Create by using the SQL INSERT statement
    # • Read by using SELECT
    # • Update by using UPDATE
    # • Delete by using DELETE

    # Basic SQL DML commands
    # Operation                                 SQL pattern                                 SQL example
    # Add a row                             INSERT INTO tbname VALUES( … )              INSERT INTO t VALUES(7, 40)
    # Select all rows and columns           SELECT * FROM tbname                        SELECT * FROM t
    # Select all rows, some columns         SELECT cols FROM tbname                     SELECT id, count FROM t
    # Select some rows, some columns        SELECT cols FROM tbname WHERE condition     SELECT id, count from t WHERE count > 5 AND id = 9
    # Change some rows in a column          UPDATE tbname SET col = value  WHERE condition  UPDATE t SET count=3 WHERE id=5
    # Delete some rows                      DELETE FROM tbname WHERE  condition         DELETE FROM t WHERE count <= 10 OR id = 16


    ### DB-API
    # DB-API is Python’s standard API for accessing relational databases.
    # connect() # Make a connection to the database;
    # cursor() - Create a cursor object to manage queries.
    # execute() and executemany() - Run one or more SQL commands against the database.
    # fetchone(), fetchmany(), and fetchall() - Get the results from execute.

    # SQLite - SQLite is a good, light, open source relational database. It’s implemented as a standard Python library,
    # and stores databases in normal files.


    ###  Create a database and a table
    # conn = sqlite3.connect('enterprise.db')  # DB is created in the current directory
    # curs = conn.cursor()
    # # curs.execute('''
    # #                 CREATE TABLE employees
    # #                 (
    # #                     emp_id INT PRIMARY_KEY,
    # #                     emp_name VARCHAR(20),
    # #                     emp_email VARCHAR(20)
    # #                 )
    # #             ''')
    # #
    # # # # insert data
    # # curs.execute('INSERT INTO employees VALUES(1, "Arun", "arun@company.org")')
    # # curs.execute('INSERT INTO employees VALUES(2, "Aditya", "aditya@company.org")')
    # # curs.execute('INSERT INTO employees VALUES(3, "Ashish", "ashish@company.org")')
    # # curs.execute('INSERT INTO employees VALUES(4, "Ankur", "ankur@company.org")')
    #
    # # curs.execute('''
    # #                 DELETE FROM employees WHERE emp_id = 1;
    # # ''')
    # #
    # #
    # # extract data
    # curs.execute('SELECT * FROM employees')
    # rows = curs.fetchall()
    # print(rows)
    #
    # # close connection and database
    # conn.commit()
    # curs.close()
    # conn.close()

    ### install DB Browser for SQLite -  https://sqlitebrowser.org/dl/
    # invoke from command line by typing sqlitebrowser
    # add to favorites


    # ### import csv into DB
    # conn = sqlite3.connect('brain.db')
    # curs = conn.cursor()
    #
    # df_data = pd.read_csv('~/ibab-repo/brain_size.csv', sep=';', na_values=".")
    # df_data.to_sql('brain_size', conn, if_exists='replace', index=False)
    #
    # conn.commit()
    # curs.close()
    # conn.close()


    ### execute SQL queries

    # # connect to DB and open a cursor for querying
    # conn = sqlite3.connect('brain.db')
    # curs = conn.cursor()
    #
    # # execute the query
    # curs.execute('SELECT * from brain_size ORDER BY FSIQ')
    # rows = curs.fetchall()
    # print(rows)
    #
    # # commit and close
    # conn.commit()
    # curs.close()
    # conn.close()


    # # update query
    # conn = sqlite3.connect('enterprise.db')  # DB is created in the current directory
    # curs = conn.cursor()
    # curs.execute('''
    #                 UPDATE employees SET emp_email = "arun1@example.com"  WHERE emp_id = 1
    #             ''')
    #
    # # commit and close
    # conn.commit()
    # curs.close()
    # conn.close()



    print('End')


   # Construct to not include whole program in other includes
if __name__ == "__main__":
   main()