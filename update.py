import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database Successfully")

conn.execute("UPDATE EMPLOYEE set SALARY = 88000.00 where ID =1")
conn.commit()

cursor = conn.execute("SELECT id,name,age,address,salary from EMPLOYEE")
for row in cursor:
    print("ID = " ,row[0])
    print("NAME = " ,row[1])
    print("AGE = " ,row[2])
    print("ADDRESS = " ,row[3])
    print("SALARY = " ,row[4])
print("Operation done Successfully")
conn.close()