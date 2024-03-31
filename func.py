'''def sum(a,b):
	summation=a+b
	print('The sum of two digits is:',summation)
sum(2,5)
sum(2.5,5.2)

def sum(a,b):
	addition=a+b
	return(addition)
q=sum(2,5)
print('The sum of two digits is:',q)
q=sum(2.5,5.2)
print('The sum of two digits is:',q)

number=int(input('Enter the number:'))
def oe(number):
	if number%2==0:
		print('The entered number is even')
	else:
		print('The entered number is odd')	
oe(number)

def pnz(number):
	if number>0:
		print('The number is positive')
	elif number==0:
		print('The number is zero')
	else:
		print('The number is negative')
number=int(input('Enter the number:'))
pnz(number)			

def arith(a,b):
	add=a+b
	sub=a-b
	multi=a*b
	div=a/b
	return add,sub,multi,div
a,s,m,d=arith(10,2)
print('The addition of two number is:',a)	
print('The substraction of two number is:',s)
print('The multiplication of two number is:',m)
print('The division of two number is:',d)

def mod(a):
	a=7
	print('The value of a,inside of function',a)
a=9
mod(a)
print('The value of a,outside of function',a)

def mod(a):
	lst.append(2)
	print(lst,id(lst))
lst=[1,2,3,4,5]
mod(lst)	

def conc(s1,s2):
	s3=s1+s2
	print(s3)
conc('Atmiya','University')
conc('University','Atmiya')
#conc('University')	

def emp(eid,name):
	print('The employee id is:',eid)
	print('The employee name is:',name)
emp(eid=101,name='abc')
emp(name='fdf',eid=101)	

def emp(eid,name='abc'):
	print('The employee is:',eid)
	print('The employee name is:',name)
emp(eid=101,name='abc')
emp(eid=102)

def addition(farg,*args):
	sum=0
	for i in args:
		sum=sum+i
	print('sum of all numbers is:',(farg+sum))
addition(2,5)
addition(2,5,9)'''

# error:======
def dis(lst):
	for i in lst:
		print(i)
print('Enter elements separated by space:',end='')
lst=[a for a in input().split()]
dis(lst)

def sqr(a):
	return(a*a)
sqr=lambda a:a*a
a=int(input('Enter the value:'))
print('The squre of entered number is:',sqr(a))

big=lambda a,b:a if a>b else b
# a=int(input('Enter the value of a:'))
# b=int(input('Enter the value of b:'))
# print('The bigger number is:',big(a,b))

# def generator(a,b):
# 	while a<=b:
# 		yield a
# 		a=a+1
# gen=generator(1,10)
# for i in gen:
# 	print(i,end='')

f=open('file1','w')
str1=input('Enter the data you want to write into the file:')
f.write(str1)
f.close()

f=open('file1','r')
str1=f.read()
print(str1)
f.close()	

f=open('file1','a')
str1=input('Enter the data you want to write into the file:')
f.write(str1)
f.close()

