#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

test= pd.read_csv("C:\\Users\\akshansh\\Desktop\\python programs\\test.csv")
print(test)


# In[15]:


test=sns.load_dataset("titanic")
test.head()


# In[16]:


sns.lineplot(x="age",y="fare",data=test,hue="sex")
plt.show()


# In[17]:


sns.lineplot(x="age",y="fare",data=test,hue="sex",style="sex")
plt.show()


# In[28]:


sns.lineplot(x="age",y="fare",data=test,hue="sex",marker='o')
plt.show()


# In[30]:


sns.barplot(x="age",y="fare",data=test,hue="sex")
plt.show()


# In[31]:


sns.barplot(x="age",y="fare",data=test,hue="sex",palette="rocket")
plt.show()


# In[54]:


plt.figure(figsize=(10,6))
sns.barplot(x="age",y="fare",data=test,hue="sex")
plt.show()


# In[65]:


plt.figure(figsize=(10,6))
sns.histplot(x="age",y="fare",data=test,hue="sex",bins=10)
plt.show()


# In[66]:


plt.figure(figsize=(10,6))
sns.scatterplot(x="age",y="fare",data=test,hue="sex")
plt.show()


# In[ ]:




