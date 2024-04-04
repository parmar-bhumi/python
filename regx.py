
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

# import re
# str1='Hello!All;good;morning'
# result=re.split(r'\w+',str1)
# print(result)

# import re
# str1='AITS is the best organisation'
# print(str1)
# result=re.sub(r'AITS','Atmiya university',str1)
# print(result)	

# import re
# str1='sun shines sooner or later'
# result=re.findall(r's[\w]*',str1)
# print(result)

# import re
# str1='The special classes are arranged on 11th and 21st of every day'
# result=re.findall(r'\d[\w]*',str1)
# print(result)

# import re
# str1='sun mon tue wed thurs fri saturday'
# result=re.findall(r'\b\w{5}\b',str1)
# print(result)

# import re
# str1='sun mon tue wed thurs fri saturday'
# result=re.findall(r'\b\w{3,4}\b',str1)
# print(result)

# import re
# str1='sun mon tue wed thurs fri saturday'
# result=re.findall(r'\b\w{3,5}\b',str1)
# print(result)

# import re
# str1='one three five seven 8 923 10 3000'
# result=re.findall(r'\b\d\{2,}\b',str1)
# print(result)

# import re
# str1='star moon starts planets galaxy star'
# result=re.findall(r's[\w]*\Z',str1)
# print(result)

# import re
# str1='star moon starts planets galaxy'
# result=re.findall(r'\As[\w]*',str1)
# print(result)

#quantifiers:====
# import re
# str1='abc:1234 cdc:1235'
# result=re.search(r'\d+',str1)
# print(result.group)

# error:====-
import re
str1=001 acc 01-10-1999,002 cde 21-10-1980,003 efg 12-11-1980
result=re.findall(r'\d{2}-\d{2}-\d{2}-\d{4}',str1)
print(result)

