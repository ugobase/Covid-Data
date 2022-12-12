#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


uno = pd.read_csv('covid data.csv')
uno


# In[3]:


uno.isnull().sum()


# In[4]:


uno.info()


# In[5]:


uno = uno.loc[:, uno.isin([' ','NaN', 0, np.nan]).mean() < .1]
uno


# In[6]:


uno.isnull().sum()


# In[7]:


uno = uno.fillna(20)
uno


# In[8]:


uno.isnull().sum()


# In[9]:


uno.describe()


# In[10]:


uno.continent.unique()


# In[11]:


uno.continent = uno.continent.replace([20], 'Africa')


# In[12]:


uno.continent.unique()


# In[13]:


uno


# In[14]:


uno.sort_values('life_expectancy', ascending = False).life_expectancy.head(10)


# In[15]:


uno.nlargest(10, ['life_expectancy'])['life_expectancy']


# In[16]:


uno.sort_values('population').head()


# In[17]:


uno.nsmallest(5,['population'])


# In[18]:


uno[uno.life_expectancy > 85].shape[0]


# In[19]:


uno[uno.location.str.contains('C')]


# In[20]:


uno[uno.location.isin(['Cambodia', 'Africa'])]


# In[21]:


uno[uno.location.str.contains('A')]


# In[22]:


uno[uno.life_expectancy > 80].total_cases.value_counts()


# In[23]:


uno[(uno['life_expectancy'] > 80)].groupby(['total_cases']).count()


# In[24]:


uno.insert(8, 'New', uno.life_expectancy.apply(lambda x: 'Old' if x > 60 else 'Young'))
uno


# In[25]:


uno[uno.date.str.contains('2022')]


# In[26]:


uno[uno.date.isin(['1/1/2022', '9/26/2022', '9/30/2022'])]


# In[27]:


uno[(uno.date > '9/26/2022')]


# In[28]:


uno.groupby('population').date.describe()


# In[29]:


uno.groupby('population').life_expectancy.describe()


# In[30]:


uno[(uno.continent == 'Africa') & (uno.life_expectancy > 80)]


# In[31]:


uno[(uno.continent == 'Europe') & (uno.life_expectancy > 86)]


# In[32]:


uno[(uno.continent == 'Europe') & (uno.population > 8.34085540e+07) & (uno.total_cases_per_million > 100000)]


# In[33]:


uno[(uno.location == 'Germany') & (uno.total_cases > 20000000) & (uno.New == 'Old')]


# In[34]:


uno[(uno.location == 'Nigeria') & (uno.total_cases > 100000) & (uno.New == 'Young')]


# In[35]:


uno.location.unique()


# In[36]:


uno.sort_values('date', ascending = False).head(20).shape[0]


# In[37]:


uno[(uno.location == 'Nigeria') & (uno.total_cases > 200000) & (uno.New == 'Young')]


# In[38]:


uno[(uno.continent == 'North America') & (uno.life_expectancy > 70) & (uno.date == '9/26/2022')]


# In[39]:


uno[(uno.continent == 'North America') & (uno.location == 'United States') & (uno.total_cases > 40000000) & (uno.population > 300000000) & (uno.New == 'Old')]


# In[40]:


uno[(uno.continent == 'North America') & (uno.location == 'United States') & (uno.date == '9/26/2022')]


# In[41]:


uno[(uno.continent == 'Oceania') & (uno.life_expectancy	 > 70) & (uno.date == '9/26/2022')]


# In[42]:


uno[(uno.iso_code.str.contains('A'))]


# In[43]:


uno[(uno.total_cases > 8000000) & (uno.life_expectancy < 25) & (uno.New == 'Young')]


# In[44]:


uno[(uno.continent == 'Asia') & (uno.life_expectancy > 84) & (uno.total_cases > 1000000)]


# In[45]:


uno[(uno.iso_code == 'JPN') | (uno.life_expectancy > 80) | (uno.location == 'China') | (uno.New == 'Young') | (uno.New == 'Old') & (uno.total_cases > 800000000)]


# In[46]:


uno[(uno.continent == 'Asia') & (uno.life_expectancy == 84.63) & (uno.location == 'Japan')]


# In[47]:


uno[(uno.continent.isin(['Asia', 'Africa']))].shape[0]


# In[48]:


uno[(uno.location.isin(['Hong Kong', 'Japan']))]


# In[49]:


plt.figure(figsize=(8,6))
sns.histplot(uno.continent)


# In[50]:


plt.figure(figsize=(8,6))
sns.boxplot(uno.population)


# In[51]:


plt.figure(figsize=(8,6))
sns.boxplot(data = uno, x = 'continent', y = 'life_expectancy')


# In[52]:


plt.figure(figsize=(8,6))
sns.boxplot(data = uno, x = 'continent', y = 'population')


# In[53]:


plt.figure(figsize=(8,6))
sns.countplot(uno.continent)


# In[54]:


plt.figure(figsize=(8,6))
sns.countplot(uno.New)


# In[55]:


plt.figure(figsize=(12,8))
sns.displot(uno.life_expectancy, kind = 'kde')


# In[56]:


uno.continent.value_counts().plot(kind = 'pie', figsize = (8,6))


# In[57]:


uno.continent.value_counts().plot(kind = 'bar', figsize = (10,6))


# In[58]:


plt.figure(figsize = (10,5))
sns.heatmap(uno.corr(), annot = True, fmt = '0.1f')


# In[ ]:




