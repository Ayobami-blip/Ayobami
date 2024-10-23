import sqlite3

connect = sqlite3.connect("data3.db")
print('database is connected successfully')

#

# connect.execute('''CREATE TABLE COMPANY
#         (ID INT PRIMARY KEY NOT NULL,       
#         NAME TEXT NOT NULL,
#         AGE INT NOT NULL,
#         ADDRESS CHAR(50),
#         SALARY INT NOT NULL);''')
# print("Table created successfully")

# connect.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#         VALUES(1,"JOHN",18,"MAYA",190000)''')
# connect.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#         VALUES(3,"JOAN",16,"MAYA",10000)''')
# connect.commit()
# print('record added')
# connect.close()

# updating the database

connect.execute("UPDATE COMPANY SET SALARY = 14000 where ID = 1 ")
connect.commit()
print('record has been updated'), connect.total_changes

cursor = connect.execute('SELECT id, name, age, address, salary FROM COMPANY')
connect.commit()
for row in cursor:
        print('ID =', row[0])
        print('NAME =', row[1])
        print('AGE =', row[2])
        print('ADDRESS =', row[3])
        print('SALARY =', row[4])

print('Operation successfully submitted')
connect.close()



import sqlite3

connect = sqlite3.connect("data3.db")
print('database is connected successfully')

connect.execute("DELETE FROM COMPANY WHERE ID = 1")

connect.commit()
print('id has been deleted')

