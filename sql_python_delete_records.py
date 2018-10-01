import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Database Connection");

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()

print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], "\n")

print("DATA Return is a success")
conn.close()