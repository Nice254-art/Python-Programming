import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS ,SALARY)\
 VALUES(1, 'Jeff', 32, 'Carlifonia', 45000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS ,SALARY)\
 VALUES(2, 'Allen', 31, 'Texas', 15000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS ,SALARY)\
 VALUES(3, 'Mark', 30, 'Norway', 145000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS ,SALARY)\
 VALUES(4, 'brendah', 30, 'Kenya', 25000.00)");

conn.commit()
print("Records created successfully")
conn.close()