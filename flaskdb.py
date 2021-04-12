import mysql.connector as b
mydb=b.connect(host="localhost",user="root",password="190330092", database="hackathon")
mycursor=mydb.cursor()
#mycursor.execute("Create Database Login")
mycursor.execute("Create table Accounts(id int(11) NOT NULL AUTO_INCREMENT, username varchar(50),password varchar(100),email varchar(150),PRIMARY KEY(id))")
