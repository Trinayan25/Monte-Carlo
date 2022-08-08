#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt 
import math
from statistics import variance 
a=34
b=0
m=345

st1=np.zeros((1000,1))
st2=np.zeros((10000,1))
st3=np.zeros((100000,1))

st1[0][0]=4
st2[0][0]=5
st3[0][0]=5

for i in range(1,17):
    st1[i][0]=((a*st1[i-1][0])+b)%m
    st2[i][0]=((a*st2[i-1][0])+b)%m
    st3[i][0]=((a*st3[i-1][0])+b)%m

st1=st1/m
st2=st2/m
st3=st3/m

for i in range(17,1000):
    st1[i][0]=st1[i-17][0]-st1[i-5][0]
    if st1[i][0]<0:  
        st1[i][0]=st1[i][0]+1

for i in range(17,10000):
    st2[i][0]=st2[i-17][0]-st2[i-5][0]
    if st2[i][0]<0:  
        st2[i][0]=st2[i][0]+1

for i in range(17,100000):
    st3[i][0]=st3[i-17][0]-st3[i-5][0]
    if st3[i][0]<0:  
        st3[i][0]=st3[i][0]+1
        


g1=np.zeros((1000,1))
g2=np.zeros((10000,1))
g3=np.zeros((100000,1))

for i in range(0,1000):
    g1[i][0]=0.5-(0.5*(math.cos(st1[i]*math.pi)))
for i in range(0,10000):
    g2[i][0]=0.5-(0.5*(math.cos(st2[i]*math.pi)))
for i in range(0,100000):
    g3[i][0]=0.5-(0.5*(math.cos(st3[i]*math.pi)))

frange = np.linspace(0,1,101)

ans1=np.zeros((401,1))
ans2=np.zeros((401,1))
ans3=np.zeros((401,1))

hist, bins = np.histogram(g1,frange)
ans1[0][0]=hist[0]
for i in range(1,100):
    ans1[i][0]=ans1[i-1][0]+hist[i]
ans1=ans1/1000

hist, bins = np.histogram(g2,frange)
ans2[0][0]=hist[0]
for i in range(1,100):
    ans2[i][0]=ans2[i-1][0]+hist[i]
ans2=ans2/10000

hist, bins = np.histogram(g3,frange)
ans3[0][0]=hist[0]
for i in range(1,100):
    ans3[i][0]=ans3[i-1][0]+hist[i]
ans3=ans3/100000

x=np.linspace(0.005,.995,100)
z=np.linspace(0,1,101)
y=[]

for i in range(0,101):
    y.append((2/math.pi)*(math.asin(math.sqrt(z[i]))))


p1=plt.plot(z,y,'-r')
p2=plt.plot(x[0:100],ans1[0:100])
plt.xlabel('Range (x)')
plt.ylabel('P(X<=x)')
plt.legend((p1[0], p2[0]), ('Original','Generated')) 
plt.show() 

p1=plt.plot(z,y,'-r')
p2=plt.plot(x[0:100],ans2[0:100])
plt.xlabel('Range (x)')
plt.ylabel('P(X<=x)')
plt.legend((p1[0], p2[0]), ('Original','Generated ')) 
plt.show()

p1=plt.plot(z,y,'-r')
p2=plt.plot(x[0:100],ans3[0:100])
plt.xlabel('Range (x)')
plt.ylabel('P(X<=x)')
plt.legend((p1[0], p2[0]), ('Original','Generated')) 
plt.show()

print("The mean for 1000 Values of Ui: ")
print(sum(g1) / len(g1))
print("The variance for 1000 Values of Ui:")
print(np.var(g1))

print("The mean for 10000 Values of Ui :")
print(sum(g2) / len(g2))
print("The variance for 10000 Values of Ui: ")
print(np.var(g2))

print("The mean for 100000 Values of Ui:")
print(sum(g3) / len(g3))
print("The variance for 100000 Values of Ui:")
print(np.var(g3))


# In[ ]:




