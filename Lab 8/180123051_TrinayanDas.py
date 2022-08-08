#!/usr/bin/env python
# coding: utf-8

# In[11]:


r=0.0002981060
t=0.0222834

test=[0.01,0.05,0.1,0.2]


import numpy as np
import matplotlib.pyplot as plt
import random
import math

def norm():
  a=random.random()
  b=random.random()
  A,B=2*a-1, 2*b-1
  x=A*A+B*B
  while x>1:
    a=random.random()
    b=random.random()
    A,B=2*a-1, 2*b-1
    x=A*A+B*B
  z=math.sqrt(-2*math.log(x)/x)
  return(z*A)


def lognormal(k):
  sum=0
  for i in range(k):
    m=norm()
    m=r+t*m
    sum=sum+m
  return sum




def main(a):
  normal=[]
  for j in range(1000):
    m=norm()
    normal.append(m)

  p=[]
  s=np.random.poisson(a,1000)
  stock=185.4
  for i in range(1000):
    k=s[i]
    if k==0:
      z=(r-(0.5*t*t))+t*normal[i]
      stock=stock*math.exp(z)
      p.append(stock)
    if k!=0:
      z=lognormal(k)
      z=z+(r-(0.5*t*t))+t*normal[i]
      stock=stock*math.exp(z)
      p.append(stock)
  q=[]
  for i in range(1000):
    q.append(i+1)

  plt.plot(q,p)
  plt.show()
  

  

print("The value of Mu ",r," The value of Sigma ",t)
print("The number of days in each stimulation is 1000 ")
print("The days of trading are all consecutive;no trading dates are skipped")
print("The initial stock price is 185.4 in all the cases")
print ("  ")


for i in range(4):
  print("The poisson process test used in this stimulation is: ", test[i])
  main(test[i])


# In[ ]:




