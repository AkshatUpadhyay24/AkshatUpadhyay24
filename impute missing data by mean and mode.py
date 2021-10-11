#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[107]:


df=pd.read_csv("C:\\Users\\akshansh\\Desktop\\python programs\\bigmart.csv")


# In[108]:


df.shape


# In[109]:


df.head(8)


# In[110]:


df.isnull().sum()


# In[111]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[112]:


df.head(8000)


# In[113]:


missing_value_var=df.isnull().sum()/df.shape[0]*100
missing_value_var


# In[114]:


missing_var=missing_value_var[missing_value_var>17.165317].keys()
missing_var


# In[116]:


df3_num=df.select_dtypes(include=['int64','float64'])
df3_num


# In[117]:


df3_num.isnull().sum()


# In[118]:


df4_num_mean=df3_num.fillna(df3_num.mean())
df4_num_mean.isnull().sum()


# In[119]:


df4_num_mean.head(8000)


# In[91]:


df5_num=df.select_dtypes(include=['object'])
df5_num


# In[120]:


df5_num.isnull().sum()


# In[121]:


df6_cat_mode=df5_num['Outlet_Size'].fillna(df5_num['Outlet_Size'].mode()[0])
df6_cat_mode


# In[125]:


df.update(df6_cat_mode)


# In[128]:


df.update(df4_num_mean)


# In[129]:


df.isnull().sum()


# In[ ]:




