import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Database Connection");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (1, 'Paul', 45, 'UTAH', 40000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (2, 'Sam', 45, 'UTAH', 40000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (3, 'Joe', 45, 'UTAH', 40000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (4, 'Blake', 45, 'UTAH', 40000.00)");

conn.commit()

print('All Records Entered')

conn.close()