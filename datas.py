import pandas as pd
df=pd.read_csv('stud.csv')
print(df)

import pandas as pd
import xlrd
df=pd.read_excel('Book1.xlsx')
print(df)

stud={'roll':[1,2,3,4,5],'name':['abc','gff','gff','acs','ded'],'city':['Rajkot','Surat','Delhi','Goa','Diu']}
import pandas as pd
df=pd.DataFrame(stud)
print(df)

import pandas as pd
stud=[(1,'acs','Rajkot'),(2,'dfd','Surat'),(3,'rfd','Delhi'),(4,'bky','Goa')]
df=pd.read_excel('Book1.xlsx')
# print(df)
# #print(df.shape())
# print(df.head())
# print(df.tail())
# print(df[2:4])
#print(df[['id','sales']])
print(df['sales'].max())
print(df['sales'].min())
print(df[df.sales>50])
print(df[df.city=='Rajkot'])
print(df[['name']] [df.city=='Rajkot'])

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
df=pd.read_excel('Bookstall.xlsx')
print(df)
x=df['Type_of_book']
y=df['Sales']
plt.bar(x,y,label='category_wise_sale_of_books',color='red')
plt.xlabel('Types of book')
plt.ylabel('Sales')
plt.title('Atmiya book store')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
x=[101,102,103,104,105,106]
y=[10010,11109,20003,25007,31010,0]
x1=[105,108,102,106,111]
y1=[20110,31109,35003,29003,39010]
plt.bar(x,y,label='Production Department')
plt.bar(x1,y1,label='QA Department',color='red')
plt.xlabel('Employee id')
plt.ylabel('Salary')
plt.title('TATA consultancy services')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
prod_sales=[24,36,29,11]
prod_name=['sedan','Hatchback','Premium','Commercial']
col=['blue','magenta','red','yellow']
plt.pie(prod_sales,labels=prod_name,colors=col)
plt.title('Tata moters')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
years=['2023','2022','2021','2020','2019']
incre_pop=[89,78,65,94,55]
plt.plot(years,incre_pop,color='red')
plt.title=('Population growth of india(last 5 years)')
plt.xlabel('Years')
plt.ylabel('Increase of population in india')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import xlrd
df=pd.read_excel('stationary.xlsx')
print(df)
year=[2021,2022,2023]
x=df['pencil']
y=df['pen']
xaxis=np.arange(len(year))
plt.bar(xaxis - 0.2,x,0.4,label='pencil')
plt.bar(xaxis + 0.2,y,0.4,label='pen')
plt.xticks=(xaxis,year)
plt.xlabel('products')
plt.ylabel('sales')
plt.title('Student store')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np 
x=np.random.randn(10)
y=np.random.randn(10)
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter diagram')
plt.show()

import matplotlib.pyplot as plt 
import numpy as numpy
x=range(1,6)
y=[1,2,4,6,2]
plt.fill_between(x,y)
plt.title('Area plt')
plt.show()

