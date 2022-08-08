#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt 
a=34
b=0
m=345


st1=[0]*1000
st2=[0]*10000
st3=[0]*100000

st1[0]=4
st2[0]=5
st3[0]=5

for i in range(1,17):
    st1[i]=((a*st1[i-1])+b)%m
    st2[i]=((a*st2[i-1])+b)%m
    st3[i]=((a*st3[i-1])+b)%m

for i in range(0,17):
    st1[i]=st1[i]/m
    st2[i]=st2[i]/m
    st3[i]=st3[i]/m



for i in range(17,1000):
    st1[i]=(st1[i-17]-st1[i-5])
    if st1[i]<0:  
        st1[i]=st1[i]+1

for i in range(17,10000):
    st2[i]=(st2[i-17]-st2[i-5])
    if st2[i]<0:  
        st2[i]=st2[i]+1

for i in range(17,100000):
    st3[i]=st3[i-17]-st3[i-5]
    if st3[i]<0:  
        st3[i]=st3[i]+1
q1=[]
w1=[]
for j in range(1,1000):
    q1.append(st1[j])
for k in range(0,999):
    w1.append(st1[k])

q2=[]
w2=[]
for j in range(1,10000):
    q2.append(st2[j])
for k in range(0,9999):
    w2.append(st2[k])
s=[]
for j in range(0,100000):
    s.append(j)
q3=[]
w3=[]
for j in range(1,100000):
    q3.append(st3[j])
for k in range(0,99999):
    w3.append(st3[k]) 
    
    

plt.scatter(w1,q1) 
plt.show()
plt.bar(s[0:1000],st1[0:1000]) 
plt.show()

plt.scatter(w2,q2)
plt.show()
plt.bar(s[0:10000],st2[0:10000]) 
plt.show()


plt.scatter(w3,q3)
plt.show()
plt.bar(s[0:100000],st3[0:100000]) 
plt.show()


# In[ ]:




