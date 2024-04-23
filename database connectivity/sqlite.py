import sqlite3
cnt=sqlite3.connect('mydb.dp')
cnt.execute('CREATE TABLE stud_data(roll integer,name varchar)')
print('Table created')

#output:====
# D:\pyhton>python sqlite.py
# Table created

cnt.execute("""
			INSERT INTO stud_data VALUES
			(1,'sunday'),
			(2,'monday'),
			(3,'tuesday'),
			(4,'friday')
			""")
print('Records inserted successfully')
cnt.commit()
cursor=cnt.execute('SELECT * from stud_data')
for i in cursor:
	print(i)

#output:====
# D:\pyhton>python sqlite.py
# Records inserted successfully
# (1, 'sunday')
# (2, 'monday')
# (3, 'tuesday')
# (4, 'friday')	

cursor=cnt.execute('SELECT * from stud_data WHERE roll>2')
for i in cursor:
	print(i)

# output:====
# D:\pyhton>python sqlite.py
# (3, 'tuesday')
# (4, 'friday')	

sql_upd="""UPDATE stud_data SET name='Wednesday' WHERE roll=3"""
cnt.execute(sql_upd)
cursor=cnt.execute('SELECT * from stud_data')
for i in cursor:
	print(i)

# output:====
# D:\pyhton>python sqlite.py
# (1, 'sunday')
# (2, 'monday')
# (3, 'Wednesday')
# (4, 'friday')	

sql_del="""DELETE from stud_data WHERE roll=3"""
cnt.execute(sql_del)
cursor=cnt.execute('SELECT * from stud_data')
for i in cursor:
	print(i)

# output:====
# D:\pyhton>python sqlite.py
# (1, 'sunday')
# (2, 'monday')
# (4, 'friday')	
