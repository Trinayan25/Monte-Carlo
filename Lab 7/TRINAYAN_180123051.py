#!/usr/bin/env python
# coding: utf-8

# In[4]:




alpha_1=0.0002981060
alpha_2=0.0225234
# alpha_1 and alpha_2 represent the mue and sigma of the model respectively

size=1000
turn=0

import random
import math
import matplotlib.pyplot as plt


def norm():
  p=random.random()
  q=random.random()
  a,b=2*p-1, 2*q-1
  x=a*a+b*b
  while x>1:
    p=random.random()
    q=random.random()
    a,b=2*p-1, 2*q-1
    x=a*a+b*b
  z=math.sqrt(-2*math.log(x)/x)
  return(z*a)


list_1=[]
list_2=[]
list_3=[]


for gen in range(size):
  stock=185.4
  normal=[]
  for i in range(14):
    m=norm()
    normal.append(m)
 
  
  
  for i in range(14):
    m=(alpha_1-alpha_2*alpha_2*0.5)+alpha_2*normal[i]
    stock=stock*math.exp(m)
    #stock=stock*(alpha_2*normal[i]+alpha_1)+stock
    if i==3:
      list_1.append(stock)
    if i==8:
      list_2.append(stock)
    if i==13:
      list_3.append(stock)
   


for i in range(3):
  if i==0:
    sum=0
    for m in range(size):
      sum=sum+list_1[m]
    print("The average of list_1 for first week is : ", sum/size)
    plt.hist(list_1,bins=50)
    plt.show()
    print("The actual stock adj closing price on 7th Oct is: 190.70	")
    print("The percentage error is : ", 100*(sum/(size*190.7)-1))
    print(" ")
    print(" ")
  if i==1:
    sum=0
    for m in range(size):
      sum=sum+list_2[m]
    print("The average of list_2 for second week is : ", sum/size)
    plt.hist(list_2,bins=50)
    plt.show()
    print("The actual stock adj closing price on 14th Oct is: 200.05")
    print("The percentage error is : ", 100*(sum/(size*200.05)-1))
    print(" ")
    print(" ")
  if i==2:
    sum=0
    for m in range(size):
      sum=sum+list_3[m]
    print("The average of list_3 for third week is : ", sum/size)
    plt.hist(list_3,bins=50)
    plt.show()
    print("The actual stock adj closing price on 21st Oct is: 203.75")
    print("The percentage error is ", 100*(sum/(size*203.75)-1))


# In[ ]:




