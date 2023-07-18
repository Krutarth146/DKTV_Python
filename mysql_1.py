import mysql.connector

mydb = mysql.connector.connect(user = 'root', password = 'mysql', host = 'localhost', database='dktv')

if(mydb.is_connected()):
    print("Connection Established")
else:
    print("Not Connected")
# print(mydb)  # <mysql.connector.connection_cext.CMySQLConnection object at 0x0000020824F224A0>
cur = mydb.cursor()

# cur.execute("CREATE DATABASE shilp")

# cur.execute("CREATE TABLE  students(name varchar(20), roll int(4), marks float(3))")

# S = "INSERT INTO students(name, roll, marks) VALUES ('%s, %d , %f')"
# dk = ("Krrish", 567, 45.90)

# cur.execute(S,dk)

# mydb.commit()