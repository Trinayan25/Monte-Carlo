#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Plotting using the parameter theta = 5")
import matplotlib.pyplot as plt
import math
t = 5
m , a=244944, 1597
sample_range=[1000,10000, 100000,1000000, 10000000]
for sample in sample_range:
  print("Plotting for the sample size: ")
  print(sample)
  print(" ")
  u=[0]
  u.pop(0)
  x=1
  for i in range(sample):
   x=(x*a)%m
   k=x/m
   if k!=1:
     k=-5*(math.log(1-k))
   elif k==1:
     k=50
   if k>=50:
     k=50
   u.append(k)
  m1=[0]
  m2=[1]
  for i in range(499999):
    m1.append(0)
    m2.append(i+2)
  for i in range(sample):
    p=u[i]/0.0001
    p=math.floor(p)
    if p==500000:
      p=499999
    m1[p]=m1[p]+1
  for i in range(500000):
    m1[i]=m1[i]/sample
    m2[i]=m2[i]/10000
  for i in range(499999):
    m1[i+1]=m1[i+1]+m1[i]
  s, var=0,0
  for r in range(sample):
    s=s+u[r]
  s=s/sample
  print("The sample mean is: ")
  print(s)
  print("  ")
  for q in range(sample):
   demo=(u[q]-s)*(u[q]-s)
   var=var+demo
  var=var/sample
  print("The sample variance is: ")
  print(var)
  print("  ")
  print("Plotting the distribution function : ")
  print("  ")
  plt.scatter(m2,m1)
  plt.show()
  print("      ")
  print("      ")
  print("      ")


# In[ ]:




