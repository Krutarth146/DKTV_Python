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

# cur.execute("CREATE TABLE sample(name varchar(20), roll int(4), salary decimal(5,3), comment varchar(100))")
# cur.execute("CREATE TABLE sample1(id int(4) AUTO_INCREMENT NOT NULL, name varchar(20) NOT NULL, roll int(4), salary decimal(5,3), comment varchar(100), PRIMARY KEY (id))")
# cur.execute("CREATE TABLE sample2(id int(4) AUTO_INCREMENT NOT NULL, name varchar(20) NOT NULL, roll int(4), CONSTRAINT INAME PRIMARY KEY (id,name))")
# cur.execute("ALTER TABLE sample ADD PRIMARY KEY (roll)")
# cur.execute("ALTER TABLE sample drop PRIMARY KEY")
# cur.execute("ALTER TABLE sample2 drop COnstraint INAME")


# cur.execute("CREATE TABLE PERSON(PERSON_ID INT(10) NOT NULL ,NAME VARCHAR(30) NOT NULL, AGE INT(4) NOT NULL, GENDER VARCHAR(10) NOT NULL, EMAIL VARCHAR(90), PRIMARY KEY (PERSON_ID))")


# cur.execute("CREATE TABLE AADHAR(AADHAR_ID INT(10) NOT NULL, A_NAME VARCHAR(30) NOT NULL, PERSON_ID INT, PRIMARY KEY (AADHAR_ID), FOREIGN KEY (PERSON_ID) REFERENCES PERSON(PERSON_ID))")




# S = "INSERT INTO PERSON (PERSON_ID, NAME, AGE, GENDER, EMAIL) VALUES (%s, %s , %s, %s, %s)"
# dk = (20, "Dev", 45, "male", "123")


# S = "INSERT INTO AADHAR VALUES (%s, %s, %s)"
# dk = (33333, "Manoj", 20)

# cur.execute(S,dk)

# mydb.commit()


# a = 1024
# num = 2

S = "INSERT INTO sample2 VALUES (%s, %s, %s)"
dk = (2, "Manoj", 10)

cur.execute(S,dk)

mydb.commit()

