import sqlite3

conn = sqlite3.connect('test.db')

print(" Something happened")

conn.execute('''CREATE TABLE EMPLOYEES
        (ID INT PRIMARY KEY     NOT NULL,
        NAME            TEXT    N0T NULL,
        AGE             INT     NOT NULL,
        ADDRESS         CHAR(50),
        SALARY          REAL);''')
print("Table created successfully");


conn.close()