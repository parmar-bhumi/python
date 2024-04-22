 import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# print(mydb)

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
# 	print(i)

D:\pyhton>python datadase.py
('information_schema',)
('mypy',)
('mysql',)
('performance_schema',)
('phpmyadmin',)
('test',)

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE stud_data(roll int,name varchar(25))')

insert data

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# my_insert_query='INSERT INTO stud_data(roll,name)VALUES(%s,%s)'
# records_to_insert=[(1,'sunday'),(2,'monday'),(3,'tuesday')]
# cursor=mydb.cursor()
# cursor.executemany(my_insert_query,records_to_insert)
# mydb.commit()
# cursor.close()
# mydb.close()

# import mysql.connector
# try:
# 	mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# 	my_insert_query='INSERT INTO stud_data(roll,name)VALUES(%s,%s)'
# 	records_to_insert=[(4,'sunday'),(5,'monday')]
# 	cursor=mydb.cursor()
# 	cursor.executemany(my_insert_query,records_to_insert)
# 	mydb.commit()
# 	print('records inserted successfully')
# except mysql.connector.Error as error:
# 	print('Faile to insert data')
# finally:
# 	if mydb.is_connected():		
# 		cursor.close()
# 		mydb.close()
# 		print('Mysql connection is closed successfully')

D:\pyhton>python datadase.py
records inserted successfully
Mysql connection is closed successfully

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM stud_data')
# myresult=mycursor.fetchall()
# for i in myresult:
# 	print(i)


D:\pyhton>python datadase.py
(1, 'sunday')
(2, 'friday')
(3, 'tuesday')
(4, 'sunday')
(5, 'monday')

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute("UPDATE stud_data SET name='friday' WHERE roll=2")
# mydb.commit()
# mydb.close()

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute("DELETE FROM stud_data WHERE roll=2")
# mydb.commit()
# mydb.close()