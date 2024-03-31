# 1. Create a list containing several strings. Take input from the user (search string); display whether
# entered string is available in the list or not.

lst='hello','world','atmiya'
a=input('Enter a string:')
print(a in lst)

# 2. Accept the string from the user; display the message whether the entered string is palindrome
# or not.

str=input('Enter a string:')
str1=(str[-1: : -1])
print(str1)
if(str==str1):
	print('The entered string is palindrone')
else:
	print('The entered string is not palindrone')	

# 3. Accept the string from the user; display the string in the reverse order.

str=input('Enter string:')
str1=str[::-1]
print(str1)


# 4. Accept the string from the user; allow user to choose from the following options and perform
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii).
# Convert to the swap case, iv). Convert to the title case

str=input('Enter a string:')
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())



# 5. Allow users to enter multiple strings in the list; arrange the entered string into alphabetical
# order and display.

st=[]
n=int(input('How many strings you want to enter:'))
for i in range(n):
	print('Enter the string:',end='')
	st.append(input())
	#print(st)
	str1=st.sort()
	print(st)

# 6. Create a tuple and display it. Enter 25 at the third position and display it again.

a=(1,2,3,4,5)
a=list(a)
a.insert(3,25)
a=tuple(a)
print(a)


# 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary, b. Display the name of Author, c. Display the Bookid,d. Display the length of the dictionary,
# f. Insert year as the new key and display the dictionary again.

library={'Bookid':101,'Title':'novel','Author':'premchand','Price':121.0,'Publisher':'cdgfhf'}
#a. Display the dictionary
print(library)
a=library.values()
print(a)
#  b. Display the name of Author, c. Display the Bookid
print(library)
#d. Display the length of the dictionary
n=len(library)
print('The length of library is:',n)
#e. Update the price
library['Price']=150
print(library)
#f. Insert year as the new key
library['year']=2025
print(library)



# 8. Create a numeric array and perform following operations on it: Add 2 to each elements,
# Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find
# max and min, find the average of all elements.

from numpy import *
a=array([10,20,30,40])
print(a)
print('Adding 2 to each elements:',a+2)
print('Subtract 3 from each element:',a-3)
print('Multiply each element with 3:',a*3)
print('Divide each element by 2:',a/2)
print(max(a))
print(min(a))
print(average(a))

# 9. Create a numeric array and do the following: append the element, pop the element, insert an
# element at the desired postion, reverse the elements in the array, convert the array to list.

from array import *
arr=array('i',[10,20,30,40])
arr.append(50)
print('append the value',arr)
arr.pop()
print('pop the element',arr)
arr.insert(3,60)
print('insert an element at the desired postion',arr)
arr.reverse()
print('reverse the elements in the array',arr)
lst=arr.tolist()
print('convert the array to list.',lst)


# 10. Accept numeric elements from the user, store it to the array and display. Ask user to enter
# search element. Display the position of the searched element.

from array import *
a=array('i',[])
print('How many elements you want to enter?',end=' ')
n=int(input())
for i in range(n):
	print('Enter the elment:',end=' ')
	a.append(int(input()))
print('Elements of array are:',a)
print('which elements you want to search?:',end=' ')
search=int(input())
try:
	position=a.index(search)
	print('the',search,'found at',position)
except valueError:
	print('the search elment is not found in array')


# 11. Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each
# array and display only the bigger number.

from numpy import *
a=array([10,20,30,40,50])
b=array([20,40,50,80,90])
c=where(a>b,a,b)
print(a)
print(b)
print(c)

# 12. Accept dimension of the array and its values from the user, create an array as desired.

from array import *
arr=array("i",[])
print('How many elements you want to enter:',end='')
n=int(input())
for i in range(n):
	print('Enter an element:',end='')
	arr.append(int(input))
print('Elements of array are:',arr)	

# 13. Create a function to calculate the simple interest.


def sim(p,r,n):
	i=(p*r*n)/100
	print('The simple interest is:',i)
sim(20,30,40)	

# 14. Create a function to perform basic arithmetic operations on the number.

def arith(a,b):
	add=a+b
	sub=a-b
	mul=a*sub
	div=a/b
	return add,sub,mul,div
a,s,m,d=arith(20,5)
print('The of addition two number is:',a)
print('The of substration two number is:',s)
print('The of multiplication two number is:',m)
print('The of division two number is:',d)


# 15. Accept multiple strings and store it into the list using function.

str=[]
str1=input("Enter multiple strings: ")
str2=str1.split()
for x in range(len(str2)):
    str.append(str2)
print(str)


# 16. Find the biggest number from three values using lambda.

big=lambda a,b:a if a>b else big
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
print('the biggest number is:',big(a,b))

# 17. Demonstrate the use of: i). break and ii). pass.

# pass statement is used in empty loops and has no effect on program flow.
# with the help of break statemt we  exit the loops.in program break is effective. 
