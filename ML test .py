#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[6]:


Uber=pd.read_csv("C:\\Users\\akshansh\\Desktop\\python programs\\Uber.csv")

print(Uber)
# In[9]:


Uber.head()


# In[11]:


Uber.shape


# In[12]:


Uber.isnull().head()


# In[17]:


sns.lineplot(x="Request id",y="Pickup point",data=Uber,hue="Pickup point")
plt.show()


# In[20]:


(pd.to_datetime('11/7/2016',dayfirst=True))


# In[ ]:




