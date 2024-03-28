#Question-1:--
a=int(input("Enter first int value:"))
b=int(input("Enter the second int value:"))
if a>b:
	print("The  first number is bigger")
if a<b:
	print("The second number  is smaller")	

#Question-2:--

number=int(input("Enter value:"))
if number%5==0:
	print("The number is divisible")
else:
	print("The number is not divisible")

#Question-3:--	

number=int(input("Enter value:"))
if number>=0 and number<=100:
	print("The number is between 0 to 100")
else:
	print("The number is not between 0 to 100")

#Question-4:--		

a=input("Enter value:")
print(a)
print(len(a))
if len(a)==4:
	print("The number is four digit")
else:
	print("The number is not four digit")

#Question-5:--

a=int(input("Enter the value:"))
if a==1:
	print("Sunday")
elif a==2:
	print("Monday")
elif a==3:	
	print("Tuesday")
elif a==4:	
	print("Wednesday")
elif a==5:	
	print("Thursday")
elif a==6:	
	print("Friday")
elif a==7:
	print("Saturday")

#Question-6:--

no1=int(input("Enter no1:"))
no2=int(input("Enter no2:"))
print("Addition is=",no1+no2)
print("Substraction is=",no1-no2)
print("Multiplication is=",no1*no2)
print("Divisible is=",no1/no2)

#Question-7:--
#Accept the string from the user; display the count of vowels and consonants.
string=str.lower(input('enter the string:'))
vowel=0
consonant=0
for a in string:
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
vowel=vowel+1
else:
consonant=consonant+1
print('the count of vowel in the string:',vowel)
print('the count of consonant in the string:',consonant)

#Question-8:--
num=int(input('enter the number for which you want to print the table of:'))
counter=1
print('the table of:',num)
while counter<=10:
print(num,'X',counter,'=',ans)
counter+=1

#Question-9:--
# Display square and cube of numbers 1-10.
print('Square:')
number=1
while(number<=10):
print(number,'\t',number**2)
number+=1
print('\n Cube:')
number=1
while(number<=10):
print(number,'\t',number**3)
number+=1


#Question-10:-- 
#Accept string from the user; convert the string to upper case.
string=str(input('Enter the string:'))
print(string.upper())
for i in range(1, 11):
print(i, end=" ")
print()
# ii. 10 to 1
for i in range(10, 0, -1):
print(i, end=" ")
print()
# iii. 1 3 5 7 9
for i in range(1, 10, 2):
print(i, end=" ")
print()
# iv. 2 4 6 8 10
for i in range(2, 11, 2):
print(i, end=" ")
print()

#Question-11:-- 
Print 1 2 4 8 16 32 64 128 256 512 1024
num = 1
for _ in range(11):
print(num, end=" ")
num *= 2

#Question-12:--  
#Accept the number from the user; display the table of that number.
num = int(input("Enter a number: "))
print("\n table of", num)
for i in range(1, 11):
print(num, "x", i, "=", num * i)

#Question-13:--  
#Accept numbers from the user; display the sum of the entered
numbers.
a=int(input('enter first number:'))
b=int(input('enter second number:'))
sum=a+b
print('sum of two number is:',sum)


#Question-14:--  
Accept numbers from the user; display the count of the entered
numbers.
n=int(input("Enter number:"))
count=0
while(n>0):
count=count+1
n=n//10
print("The number of digits in the number are:",count)

#Question-15:--  
#Accept numbers from the user; find and display number of zeros
available in the number.
number = input("Enter a number: ")
zero_count = 0
for digit in number:
if digit == '0':
zero_count += 1
print("Number of zeros in the input number:", zero_count)


#Question-16:--  
#Accept an integer from the user; tell user that whether entered number
is even or odd.
Required output:
Enter the number: 7
7 is an odd number
Do you want to check another number? Y
Enter the number: 2
2 is an even number
Do you want to check another number? N
while True:
number = int(input("Enter the number: "))
if number % 2 == 0:
print(number,"number is an even number")
else:
print(number,"number is an odd number")
check_another = input("Do you want to check another number? (Y/N): ")
if check_another.lower() != 'y':
break


