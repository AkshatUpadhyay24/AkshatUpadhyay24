#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd


# In[40]:


df=pd.read_excel("C:\\Users\\akshansh\\Desktop\\python programs\\Promotion.xlsx")


# In[41]:


df.shape


# In[42]:


df.head()


# In[44]:


df.columns


# In[49]:


df.drop(['Credit card spent ($)', 'Type of promotion'],axis=1,inplace=True)


# In[50]:


df.columns=['Stacked','Unstacked']


# In[51]:


df.head()


# In[58]:


df.shape


# In[66]:


df.isnull().sum()


# In[67]:


df=df.dropna()


# In[68]:


df.isnull().sum()


# In[72]:


df.shape


# In[73]:


df.boxplot()


# In[74]:


from scipy.stats import ttest_1samp


# In[75]:


ttest_1samp(df,250)


# In[76]:


df.mean()


# In[77]:


df.describe()


# In[ ]:




