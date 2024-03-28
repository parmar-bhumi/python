# from array import *
# c= array('u',['a','c','d','e','b'])
# for ch in c:
# 	print(ch)

# from array import *
# c= array('u',['a','c','d','e','b'])
# d=array(c.typecode,(a for a in c))
# for ch in d:
# 	print(ch)

# from array import *
# a=array('i',[4,5,6,7,9,8])
# n=len(a)k 
# print(n)
# i=0
# while i<n:
# 	print(a[i],end=',')
# 	i=i+1

# from array import *
# c= array('u',['a','t','m','i','y','a','u','n','i','v','e','r','s','i','t','y'])
# a=c[1:16]
# print(a) 	
# a=c[0:]
# print(a) 	
# a=c[:16]
# print(a) 	
# a=c[:4]
# print(a) 	
# a=c[2:5]
# print(a) 	
# a=c[-16:]
# print(a) 	
# a=c[-16:-5]
# print(a) 	
# a=c[0:16:2]
# print(a) 	
# from array import *
# a=array('i',[10,20,30,40])
# n=len(a)
# print(n)
# i=0
# while i<n:
# 	print(a[i],end=' ')
# 	i=i+1

# from array import *	
# ar=array('i',[1,2,3,4])
# print('the initial value of an array is',ar)
# ar.append(7)
# print('an array values after append is:',ar)
# ar.insert(4,9)
# print('values after inserting is:',ar)
# ar.remove(2)
# print(ar)
# ar.pop()
# print(ar)
# als=ar.tolist()
# print(als)

# from array import *
# str=input('Enter marks:').split(',')
# marks=[int(num)for num in str]
# total=0
# for a in marks:
# 	print(a)
# 	total=total+a
# print('total score is:',total)	
# l=len(marks)
# percent=total/l
# print('the percent is:',percent)

# from array import *
# a=array('i',[])
# print('How many elements you want to enter?',end=' ')
# n=int(input())
# for i in range(n):
# 	print('Enter the elment:',end=' ')
# 	a.append(int(input()))
# print('Elements of array are:',a)
# print('which elements you want to search?:',end=' ')
# search=int(input())
# try:
# 	position=a.index(search)
# 	print('the',search,'found at',position)
# except valueError:
# 	print('the search elment is not found in array')		

# from numpy import *
# ar=linspace(2,10,5)
# print(ar)
# from numpy import *
# ar=arange(1,10,2)
# print(ar)
# from numpy import *
# ar=linspace(2,10,5)
# print(ar)

# from numpy import *
# a=array([2,10,50,30,40,50])
# print(a)
# print('Adding 5 to each elements of an array:',a+5)
# print('substracting 5 to each elements of an array:',a-5)
# print('multiplying 5 to each elements of an array:',a*5)
# print('dividing each elements  with 5 in array:',a/5)
# print('finding maximum value from the array:',max(a))
# print('finding sum value from the array:',sum(a))
# print('finding avg/mean value from the array:',mean(a))

# from numpy import *
# a=array([2,3,4,5])
# b=array([5,4,3,2])
# print('hello',a>b)
# print('hello',a>=b)
# print('hello',a<b)
# print('hello',a<=b)
# print('hello',a!=b)
# print('hello',a==b)

# from numpy import *
# a=array([1,2,3,4,5,6,7])
# b=array([2,1,4,5,6,3,7])
# c=where (a>b,a,b)
# print(a)
# print(b)
# print(c)

# from numpy import *
# a=array([1,2,3,4,0,6,7])
# b=nonzero(a)
# # print(a)
# # print(b)
# print(a[b])

# from numpy import *
# a1=array([10,20,30,40,50,60,70,80,90,100])
# b1=a1.view()
# print('Elements of an array a1 are:',a1)
# print('Elements of an array b1 are:',b1)
# b1[4]=500
# print('Elements of an array b1 after the modification are:',b1)
# print('Elements of an array a1 after the modification are:',a1)
# print(id(a1))
# print(id(b1))

# string=str.lower(input('Enter the string:'))
# vowel=0
# consonant=0
# for a in string:
# 	if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
# 		vowel=vowel+1
# 	else:
# 		consonant=consonant+1	
# print('The count of vowels in the string:',vowel)
# print('The count of consonant in the string:',consonant)

# from numpy import *
# a=array([10,20,30,40,50])
# b=a.copy()
# print('Elements of an array a are:',a)
# print('Elements of an array b are:',b)
# b[2]=3
# print('Elements of an array a are:',a)
# print('Elements of an array b are:',b)

# from numpy import *
# a=array([10,20,30,40,50,60,70,80,90,100])
# print(a)
# print(a[0:6:2])
# print(a[::])
# print(a[2: :2])
# print(a[2:])

# from numpy import *
# a=array([10,20,30,40,50,60,70,80,90,100])
# print(a)
# i=0
# while(i<len(a-1)):
# 	print(a[i],end=' ')
# 	i=i+1

# from numpy import *
# a=array([10,20,30,40,50,60,70,80,90,100])
# print(a.reshape(2,5))
# print(a.flatten())
# print(a.size)
# b=array([[10,20,30,40],[60,70,80,90],[87,88,88,66],[90,99,99,88]])
# print(b.shape)
# print(b.size)

# from numpy import *
# a=array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# b=reshape(a,(6,2))
# print(b)
# c=reshape(a,(2,2,3))
# print(c)

# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# for i in range(len(a)):
# 	print(a[i])
# for i in range(len(a)):
# 	for j in range(len(a[i])):
# 		print(a[i][j])	

# from numpy import *
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[0,:])
# print(a[1,:])
# print(a[:0])
# print(a[0:1,0:1])
# print(a[2:3,1:2])

# s1='welcome to atmiya university,rajkot'
# s2='welcome to atmiya university,rajkot'
# print(s1)
# print(s2)
# s3='welcome to "atmiya university",rajkot'
# print(s3)
# s4='welcome to \t "atmiya university", \n rajkot'
# print(s4)
# s5=r'welcome to \t "atmiya university", \n rajkot'
# print(s5)
# print(len(s1))
# print(s1*2)
# s6='Atmiya'
# s7='University'
# st=s6+s7
# print(st)

# st='Atmiyauni'
# n=len(st)
# i=0
# while i<n:
# 	print(st[i],end=' ')
# 	i=i+1
# print('uni  dabo nthi')

# st='Atmiyauni'
# #n=len(st)
# i=0
# for i in st[ : :-1]:
# 	print(i,end=' ')
# print()

# st='Atmiyauni'
# print(st[0:17:1])
# print(st[0:17:2])

# st=input('Enter the main string:')
# substr=input('Enter the main string you want to find from main string:')
# if substr in st:
# 	print(substr,'is available in the main string')
# else:
# 	print(substr,'is not available in the main string')	

# st=input('Enter the string to check:')
# st1=(st[-1::-1])
# print(st1)
# if(st==st1):	
# 	print('The entered string is palindrome')
# else:
# 	print('The entered string is not palindrome')	

# st='Better India for Better world'
# n=st.count('Better',0,23)
# print(n)
# n=st.count('Better')
# print(n)

# s='hello world'
# s1='India'
# s2='Gujrat'
# print(s)
# s=s.replace(s,s2)
# print(s)

# st='your future is bright'
# print(st.upper())
# print(st.lower())
# print(st.swapcase())
# print(st.title())
# m_number=input('Enter your mobile number:')
# print(m_number.isdigit())
# if m_number.isdigit()!=True:
# 	print('Enter valid mobile number')

# st=[]
# n=int(input('How many strings you want to enter?:'))
# for i in range(n):
# 	print('Enter the string:',end=' ')
# 	st.append(input())
# 	#print(st)
# 	#st1=st.sort()
# 	#print(st)
# 	for i in st:
# 		print(i)

# sr=input('Enter a character:')
# ch=st[0]
# if ch.isalpha():
# 	print('It is an alphabet')
# 	if ch==ch.upper():
# 		print('You have entered in upper case')
# 	else:
# 		print('you have entered in lower case')
# else:
# 	print('please enter some alphabet')	

#List:-========================
# lst=range(1,11,2)
# for i in lst:
# 	print(i,'',end=' ')	

# lst=list(range(1,11))
# print(lst)		
# lst.append(11)
# print(lst)	
# lst.remove(5)
# print(lst)	
# a=lst.index(7)
# print(a)
# lst.clear()
# print(lst)
# n=len(lst)
# print(n)

# lst=['apple','banana','mango','papita']
# lst.reverse()
# print(lst)

# a=[10,20,30,40]
# b=['sun','mon','tue','wed']
# print(a+b)

# a=[10,20,30,40]
# print(a*5)

# ls=[10,20,30,40,50]
# a=7
# b=30
# print(a in ls)
# print(b in ls)
# print(a not in ls)
# print(b not in ls)

# ls=[10,20,30,40,50]
# ls1=ls[:]
# print(ls1)
# ls[3]=400
# print(ls)
# print(ls1)

# a=[]
# n=int(input('How many times an element you want to enter?:'))
# for i in range(n):
# 	print('Enter an element:',end=' ')
# 	a.append(int(input()))
# print('The elements of list are:',a)
# find=int(input('Enter an element to found:'))
# cnt=0
# for i in a:
# 	if(find==i):
# 		cnt=cnt+1
# print('{} is found {} time(s).'.format(find,cnt))

# fruits1=['mango','grapes','apple']
# fruits2=['watermalon','pinapple','kamalam','apple']
# s1=set(fruits1)
# s2=set(fruits2)
# print(s2)
# # s=s1.intersection(s2)
# print(s)	
# common=list(s)
# print(common)

#Tuple:===============
# a=(1,)
# print(a)
# a=(1)
# print(a)
# a=10,20,'atmiya','rajkot'
# print(a)

# ls=[10,20,30,40,50,60]
# tpl=tuple(ls)
# print(ls)
#print(tpl[1:6:2])

# tpl=[10,20,30,40,50,60,70,80,90,100]
# print(tpl)
# print(len(tpl))
# print(min(tpl))
# print(max(tpl))
# print(tpl.count(30))
# print(tpl.index(40))
# tpl1=[5,6,7,8,7,3,6,9,334,6,5,99,66]
# print(sorted(tpl1))
# print(sorted(tpl1,reverse=True))

# employees=((1,'abc',30000),(2,'cde',40000),(3,'frd',50000))
# print(employees)
# print(employees[2])
# print(sorted(employees,reverse=True))

# num=('s','g','c','d','g')
# lst=input('Enter the new number:')
# new_num=tuple(lst)
# pos=int(input('Enter the position:'))
# temp_num=num[0:pos-1]
# print(temp_num)
# temp_num=temp_num+new_num
# print(temp_num)
# num=temp_num+num[pos -1:]
# print(num)

# num=(1,2,3,4)
# print(num)
# lst=list(num)
# print(lst)
# a=int(input('Enter an position to insert:'))
# lst[a]=int(input('Enter an elements to insert:'))
# print(lst)
# num=tuple(lst)
# print(num)

dic={'Eid':101,'Name':'abc','sal':100000,'Dept':'Mca'}
print(dic)
print('The name of employee is:',dic['Name'])
print('The employee id is:',dic['Eid'])
n=len(dic)
print('Numbers of elements in the dictionaryn are:',n)
dic['city']:'Rajkot'
print(dic)
dic['sal']=15000
print(dic)
del dic['Name']
print(dic)
print('Name' in dic)
print('Name' not in dic)

dic={'Eid':101,'Name':'abc','sal':100000,'Dept':'Mca'}
print(dic)
dic1=dic.copy()
print(dic1)
a=dic.values()
print(a)
a=dic.keys()
print(a)
print(dic.get('sal'))
dic.update({'eid':1001})
print(dic)
dic.pop('Name')
print(dic)
#dic=clear()
#print(dic)

marks={}
print('How many subjects you want to enter?:',end='')
n=int(input())
for i in range(n):
	print('Enter subject:',end='')
	key=input()
	print('Enter marks:',end='')
	value=int(input())
	marks.update({key:value})
print('subjects and respective marks are:',marks)
total=sum(marks.values())
print('Total marks',total)


name_object=['lotus','mango','tiger']
category=['Flowers','Fruits','Animal']
a=zip(category,name_object)
print(type(a))
d=dict(a)
print(d)

st='1=abc,2=fff,3=ffd'
print(st)
lst=[]
for i in st.split(','):
	j=i.split('=')
	lst.append(j)
print(lst)
dictionary=dict(lst)
print(dictionary)
print(type(dictionary))

dic1={}
for key,values in dictionary.items():
	dic1[int(key)]=values
print(dic1)
print(type(dic1))		

dic={'eid':101,'name':'abc','dept':'mca','sal':1000}
print(dic)

from collections import OrderedDict
dic=OrderedDict()
dic['eid']=101
dic['name']='adc'
dic['dept']='mca'
for i,j in dic.items():
	print(j,i)
print(type(dic))	

dic={9:'abc',1:'frd',2:'gdr',3:'gde'}
print(dic)
d1=sorted(dic.items(),key=lambda a:a[0])
print(d1)
d1=sorted(dic.items(),key=lambda a:a[1])
print(d1)

x=lambda a,b:a+b
print(x(2,3))


