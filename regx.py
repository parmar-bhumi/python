
# from zipfile import *
# f=Zipfile('abc.zip','w',ZIP_DEFLATED)
# f.write('stationary_store.jpeg')
# f.write('download.png')
# f.close()

# with open('stud_reg_dat','wb')as f:
# 	n=int(input('How many records to enter?:'))
# 	for i in range(n):
# 		enr=input('Enter enrollment number:')
# 		name=input('Enter name:')
# 		enr=enr.encode()
# 		name=name.encode()
# 		f.write(enr+name)
# import mmap,sys
# print('1,to view all the data of file')		
# print('2,to view enrollment number')
# print('3,to modify the entry')
# print('4,to exit')
# ch=input('Enter your choice:')
# if ch=='4':
# 	sys.exit()
# with open('stud_reg_dat','r+b') as f:
# 	mm=mmap.mmap(f.fileno(),0)	
# 	if(ch=='1'):
# 		print(mm.read().decode())
# 	if(ch=='2'):
# 		name=input('Enter the name of student to view his/her enrollment number:')
# 		n=mm.find(name.encode())
# 		n1=n+len(name)
# 		enrol=mm[n1:n1+4]
# 		print('The enrollment number is :',enrol.decode())
# 	if(ch=='3'):
# 		name=input('Enter the name of student to modify his/her enrollment number:')
# 		n=mm.find(name.encode())
# 		n1=n+len(name)
# 		new_enrol=input('Enter the updated enrollment number:')
# 		mm[n1:n1+4]=new_enrol.encode()
# 	mm.close()			

# str='This will be printed on the \n new line'
# print(str)
# str1=r'This will be printed number \n new line'
# print(str1)

# import re
# prog=re.compile(r'm\w\w')
# str1='net cat mat matter'
# result=prog.search(str1)
# print(result.group())

# import re
# str1='net cat mat matter'
# result=re.findall(r'm\w\w',str1)
# print(result)

import re
str1='Hello!All;good;morning'
result=re.split(r'\w+',str1)
print(result)

# import re
# str1='AITS is the best organisation'
# print(str1)
# result=re.sub(r'AITS','Atmiya university',str1)
# print(result)	

