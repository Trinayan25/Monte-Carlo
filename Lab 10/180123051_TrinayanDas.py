#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import math
import random
import statistics

size=[100,1000,10000,100000]

range_1=[]
range_2=[]

print("Without arithmetic variates: ")
print(" ")


for test in size:
  sample=[]
  for i in range(test):
    l=random.random()
    l=math.sqrt(l)
    l=math.exp(l)
    sample.append(l)
  p=statistics.mean(sample)
  s=math.sqrt(statistics.variance(sample))
  print("Sample size is :", test)
  print("Sample Mean is :", statistics.mean(sample))
  print("Sample Variance is :", statistics.variance(sample))
  print("Sample Standard Deviation is :", math.sqrt(statistics.variance(sample)))
  print("Sample 95% confidance interval {",p-(1.96*s)/math.sqrt(test),",", p+(1.96*s)/math.sqrt(test),"}")
  range_1.append((2*1.96*s)/math.sqrt(test))
  print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("With arithmetic variates: ")
print("    ")

for test in size:
  sample=[]
  for i in range(test):
    l=random.random()
    z=l

    l=math.sqrt(l)
    
    l=math.exp(l)
    k=math.sqrt(1-z)
    k=math.exp(k)
    l=(l+k)/2
    sample.append(l)
  p=statistics.mean(sample)
  s=math.sqrt(statistics.variance(sample))
  print("The sample size is: ", test)
  print("The sample Mean is: ", statistics.mean(sample))
  print("The sample Variance is: ", statistics.variance(sample))
  print("The sample Standard Deviation is :", math.sqrt(statistics.variance(sample)))
  print("Sample 95% confidance interval {", p-(1.96*s)/math.sqrt(test),",", p+(1.96*s)/math.sqrt(test),"}")
  range_2.append((2*1.96*s)/math.sqrt(test))
  print("    ")
  

print("The comparison of 95% confidence intervals : ")
for i in range(4):
  print("The sample size =", size[i],";", "The ratio of length of confidence intervals to that of controlled sample is :", range_1[i]/range_2[i])
 


# In[ ]:




