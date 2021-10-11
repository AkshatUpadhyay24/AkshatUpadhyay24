#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


df=pd.read_csv("C:\\Users\\akshansh\\Desktop\\python programs\\matches.csv")


# In[21]:


print(df)


# In[22]:


df.shape


# In[23]:


df.head(6)


# In[25]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[26]:


df.head(6)


# In[31]:


df.isnull().sum()


# In[71]:


plt.figure(figsize=(10,8))
sns.heatmap(df.isnull())


# In[40]:


null_var=df.isnull().sum()/df.shape[0]*100
null_var


# In[41]:


drop_columns = null_var[null_var>0.264550].keys()
drop_columns


# In[42]:


df2_dropclm=df.drop(columns=drop_columns)


# In[45]:


df2_dropclm


# In[46]:


df2_dropclm.shape


# In[47]:


sns.heatmap(df2_dropclm.isnull())


# In[48]:


df3_drop_rows=df2_dropclm.dropna()


# In[49]:


df3_drop_rows.shape


# In[50]:


sns.heatmap(df3_drop_rows.isnull())


# In[78]:


df3_drop_rows.isnull().sum()


# In[52]:


df3_drop_rows.isnull().sum().sum()


# In[54]:


df3_drop_rows.select_dtypes(include=['int64','float64']).columns


# In[55]:


sns.distplot(df['dl_applied'])


# In[56]:


sns.distplot(df3_drop_rows['dl_applied'])


# In[57]:


sns.distplot(df['dl_applied'])
sns.distplot(df3_drop_rows['dl_applied'])


# In[73]:


num_var=['dl_applied', 'win_by_runs', 'win_by_wickets']
plt.figure(figsize=(10,5))
for i,var in enumerate(num_var):
    plt.subplot(1,3,i+1)
    sns.distplot(df[var],bins=10)
    sns.distplot(df3_drop_rows[var],bins=10)


# In[75]:


df3_drop_rows.select_dtypes(include=['object']).columns


# In[76]:


df3_drop_rows.head(6)


# In[ ]:




