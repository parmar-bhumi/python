# Get the basic salary from the employee and display the net salary by calculating the following
# conditions: Applicable TA 4%, DA 30%, HRA 15% on basic salary. Applicable 3% tax, 12% PF on
# basic salary.
salary=int(input('Enter your salary'))
ta=(salary*4)/100
da=(salary*30)/100
hra=(salary*15)/100
gross_salary=(salary+ta+da+hra)
print(gross_salary)
tax=(gross_salary*3)/100
pf=(gross_salary*12)/100
deduct=(gross_salary-tax-pf)
net_salary=(gross_salary-deduct)
print(net_salary)

# 2. Get the marks of 5 subjects at the command line and display the total of marks, and percentage.
import sys
sub1=int(sys.argv[1])
sub2=int(sys.argv[2])
sub3=int(sys.argv[3])
sub4=int(sys.argv[4])
sub5=int(sys.argv[5])
total=sub1+sub2+sub3+sub4+sub5
average = total / 5
print('total is:',average)
percentage=(average / 500) * 100
print(percentage)


# 3. Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water
# is being delivered by the Corporation on per litre charges as below:
# Upto 90 litres – Rs. 0/ltr
# Upto 150 litres – Rs. 2/ltr
# Upto 250 litres – Rs. 5/ltr
# More than 250 – Rs. 10/ltr
# Accept unit consumption from consumer and display the bill amount.
litre=int(input("enter the number of litres:"))
if litre<=90:
charge=0
print('no charges',charge)
elif litre<=150:
charge=(litre+2)
print('you need to pay',charge)
elif litre<=250:
charge=(litre+5)
print('you need to pay',charge)
elif litre>250:
charge=(litre+10)
print('you need to pay',charge)



# 4. A tuition class owner wants to make a simple application to allocate grade to the students on
# the basis of marks student have scored. Accept marks from the students.
# Marks more than 90 – A1 grade
# Marks 80 or less than or equal 90 – A grade
# Marks 70 or less than or equal 80 – B1
# Marks 60 or less than or equal 70 – B
# Marks 50 or less than or equal 60 – Can do Better!
# Marks <50 – Need to work hard.
marks=int(input('Enter a number:'))
if marks>90:
print('A1 Grade')
elif marks>=80 and marks<=90:
print('A Grade')
elif marks>=70 and marks<=80:
print('B1 Grade')
elif marks>=60 and marks<=70:
print('B Grade')
elif marks>=50 and marks<=60:
print('You can do better')
else:
print('Need to work hard')		


# 5. Income Tax department wants to make an application that calculates tax on the basis of the
# income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
# The tax slab is as below:
# Income up to 8 lakhs – No tax
# Income more than 8 lakh and less than 10 lakhs – 15% of income
# Income more than 10 lakhs and less than 20 lakhs – 20% of income
# Income more than 20 lakhs – 30% of income
income=int(input('Enter the income:'))
if income<=800000:
tax=0
print('no tax pay ',tax)
elif income>800000 and income<1000000:
tax=(income*15)/100
print('you need to pay 15% Of tax Rs.',tax)
elif income>=1000000 and income<2000000:
tax=(income*20)/100
print('you need to pay 20% Of tax Rs.',tax)
elif income>=2000000:
tax=(income*30)/100
print('you need to pay 30% Of tax Rs.',tax)

# 6. Accept two integer values in separate variable, display the small value and big value out of it.
value1=int(input('enter a number:'))
value2=int(input('enter a number:'))
if value1>value2:
print('Value1 is Greater')
elif value1<value2:
print('Value1 is Smaller')
elif value1==value2:
print('Both value is Equal')
else:
print('Please give a values')


# 7. Accept marks from 4 students, display which mark is highest among all.
# num_students = 4
# marks_list = [float(input(f"Enter marks for Student {i + 1}: ")) for i in range(num_students)]
# highest_mark = max(marks_list)
# print("Highest Mark among 4 students:", highest_mark)
student1=int(input('Enter marks of student1:'))
student2=int(input('Enter marks of student2:'))
student3=int(input('Enter marks of student3:'))
student4=int(input('Enter marks of student4:'))
if student1>student2 and student1>student3 and student1>student4:
print('Student1 Get highest marks')
if student2>student1 and student2>student3 and student2>student4:
print('Student2 Get highest marks')
if student3>student1 and student3>student2 and student3>student4:
print('Student3 Get highest marks')
if student4>student1 and student4>student2 and student4>student3:
print('Student4 Get highest marks')


# 8. An online selling app wants to develop a application to calculate shipping charges on the
# purchase. Accept amount from the user and calculate the shipping charges.
# The shipping charges are as below:
# Shopping amount less than 1500 – The shipping charges is Rs. 100/-
# --Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
# --Please pay (amount+100)
# Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/-
# --Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
# --Please pay (amount+70)
# Shopping amount more than 3000 – Free shipping + 7% discount on amount
# --Type a message: You saved (amount*7/100)
# --Please pay (amount – discount)
amount=int(input('enter an amount:'))
if amount<1500:
        charges=(amount+100)
        print('Please purchase (1500-amount) to avail shipping charge of Rs. 80/- '+'please pay',charges)
elif amount>1500 and amount<3000:
        charges=(amount+70)
        print('Please purchase (3000-amount) to avail shipping charge of Rs. 50/-'+'please pay',charges)
elif amount>3000:
dis=(amount*7)/100
final=(amount-dis)
print('You saved (amount*7/100)'+'please pay',final)