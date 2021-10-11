#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd
import matplotlib . pyplot as plt
import seaborn as sns


# In[20]:


header_name= ['age', 'year_of_treatment', 'positive_lymph_nodes', 'survival_5yr']
haberman=pd.read_csv("C:\\Users\\akshansh\\Desktop\\python programs\\haberman.csv",header=None,skiprows=1,names=header_name)


# In[21]:


haberman.head(8)


# In[5]:


haberman.shape


# In[6]:


haberman.survival_5yr.value_counts()


# In[31]:


sns.FacetGrid(haberman,hue='survival_5yr',size=6).map(sns.distplot,"age").add_legend()


# In[32]:


sns.FacetGrid(haberman,hue='survival_5yr',size=6).map(sns.distplot,"year_of_treatment").add_legend()


# In[33]:


sns.FacetGrid(haberman,hue='survival_5yr',size=6).map(sns.distplot,"positive_lymph_nodes").add_legend()


# In[ ]:




