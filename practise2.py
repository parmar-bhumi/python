'''a=float(input('enter first side :'))
b=float(input('enter second side :'))
c=float(input('enter third side :'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of triangle is= 0.2%f ' %area)'''


#1)find area of triangle:---
a=float(input('enter first side :'))
b=float(input('enter second side :'))
area=0.5*a*b
print('the area of triangle is',area)

#2)find area of squre:----
side=float(input('Enter the side :'))
area=side*side
print("area of squre is=",area)

#3)convert celcius to feranhit:---
celsius=float(input('Enter the celsius :'))
farenhit=(celsius*9/5)+32
print("Temp in farenhit=",farenhit)

#4)convert us dollar to indian rupees:---
dollar=float(input('Enter dollar :'))
rupees=dollar*82
print("Dollar to indian rupees=",rupees)

#5)convert litre into millilitre:---
quantity=int(input('Enter litre :'))
ml=quantity*1000
print("Convert l into ml=",ml)

#6)binary,hexa,octal convert to decimal:--
no1='10111'
no2='325'
no3='D214'
i=int(no1,2)
print(i)
i=int(no2,8)
print(i)
i=int(no3,16)
print(i)

#7)one int from user,convert binary,hexa,octal:---
	a=int(input("Enter value :"))
	binary=bin(a)
	octal=oct(a)
	hexadecimal=hex(a)
	print(binary)
	print(octal)
	print(hexadecimal)

#8)take value from user perform operation:--
a=input("Enter a string :")
print(a)
print(a[0])	
print(a[:-33])
print(a[0:25])
print(a[-1])

#9)Create bytes, enter some values and display all elements.
a=[4,5,6,9]
b=bytes(a)
print(b) 

#10)Create bytearray, enter some values and perform the following: i). Replace the 3rd element with 7, ii). Display the 5th element.
a=[5,8,4,45,67,8]
b=bytearray(a)
print(b)
b[2]=7
print(b)
print(b[4])


#11) Create list and insert values. i).Display all the elements. ii). Display the 3rd element,iii). Replace the 4th element with ‘Atmiya’, 
#iv). Display elements from 3rd to 7th element.
lst=[4,7,'hello',7,99,23,-76,7,'h']
print(lst)
print(lst[2])
lst[3]='Atmiya'
print(lst)
print(lst[2:7])

#12)Create tuple and insert values. i). Try to replace the 3rd element with 9, ii). Display the 5th element.
a=(4,7,'atmiya',7,8,0,67,'a',8)
print(a)
print(a[4])
a[2]=9
print(a)

#13) Create a set insert some values. i). Add elements to it and display, ii). Remove elements from it and display.
set={6,9,8,5,3,8,}
print(set)
set.update([10,12])
print(set)
set.remove(3)
print(set)

#14) Create a set insert some values and convert it to frozenset. Try to add and remove some elements.
a={5,3,77,34,2,4,2,4}
print(a)
fs=frozenset(a)
print(fs)
#we cannot update or remove frozenset

#15)Create an empty dictionary, Insert some Roll:Name into it. i). Retrieve 5th value using key, ii).
# Retrieve all the roll numbers, iii). Retrieve all the names, iv). Change the name of the student
# having roll no. 7, v). Remove roll no 9, vi). Display the dictionary.
dic={}
print(dic)
dicnry={1:'abc',2:'dgg',3:'tsc',4:'vhh',5:'bfg',6:'ggf',7:'hgf',8:'dsa',9:'xvx'}
print(dicnry)
print(dicnry[5])
print(dicnry.keys())
print(dicnry.values())
dicnry[7]='john'
print(dicnry)
del dicnry[9]
print(dicnry)

#16)Create a list having names of months. i). Check whether December is in list or not, ii). Query the
#list using ‘not in’.
lst=('jan','feb','mar','april','march')
print(lst)
print('dec' in lst)
print('dec' not in lst)

#17)Take two integer values from the user using split(), perform basic arithmetic operation on the values.
int1,int2=[int(no) for no in input('Enter two integer values by giving comma:').split(',')]
print('The sum of two integer values is:',int1+int2)
print('The difference of two integer values is:',int1-int2)
print('The multi of two integer values is:',int1*int2)
print('The division of two integer values is:',int1/int2)


