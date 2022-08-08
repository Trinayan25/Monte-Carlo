#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt 
import math
import numpy as np
b=100000
alpha_1=[1,2,3,4,5]
alpha_2=[6,7,8,9,10]
maximum=[]
function=[]
for num in range(0,5):
    B=(math.gamma(alpha_1[num])*math.gamma(alpha_2[num]))/(math.gamma(alpha_1[num]+alpha_2[num]))
    maximum.append((alpha_1[num]-1)/(alpha_1[num]+alpha_2[num]-2))
    function.append((1/B)*(maximum[num]**(alpha_1[num]-1))*((1-maximum[num]**(alpha_2[num]-1))))
    u1=np.random.rand(1,b)
    u2=np.random.rand(1,b)
    y=[]
    for a in range(0,b):
         if (function[num]*u2[0][a])<=((1/B)*(u1[0][a]**(alpha_1[num]-1))*((1-u1[0][a])**(alpha_2[num]-1))):
                    y.append(u1[0][a])
    plt.hist(y)
    
    plt.show()


# In[ ]:




