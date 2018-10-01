import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Database Connection");

conn.execute("UPDATE COMPANY set SALARY = 45000.00 where ID = 1")
conn.commit()

print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], "\n")

print("DATA Return is a success")
conn.close()

conn.close()