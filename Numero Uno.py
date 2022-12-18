#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:

#Reading the csv file
uno = pd.read_csv('covid data.csv')
uno


# In[3]:

#Finding missing values in dataset
uno.isnull().sum()


# In[4]:

#General information of dataset to know the datatypes
uno.info()


# In[5]:

#Data cleanup
uno = uno.loc[:, uno.isin([' ','NaN', 0, np.nan]).mean() < .1]
uno


# In[6]:

#Checking for null values
uno.isnull().sum()


# In[7]:

#Filling up all null values
uno = uno.fillna(20)
uno


# In[8]:

#Checking for null values 
uno.isnull().sum()


# In[9]:

#Statistical description of dataset
uno.describe()


# In[10]:

#Unique values of continent
uno.continent.unique()


# In[11]:

#Replacing an integer in continent with a value
uno.continent = uno.continent.replace([20], 'Africa')


# In[12]:

#Unique values in continent
uno.continent.unique()


# In[13]:

#Viewing of the dataset
uno


# In[14]:

#Top 10 values of life expectancy
uno.sort_values('life_expectancy', ascending = False).life_expectancy.head(10)


# In[15]:

#Alternative to previous
uno.nlargest(10, ['life_expectancy'])['life_expectancy']


# In[16]:

#Least 5 values of population
uno.sort_values('population').head()


# In[17]:

#Alternative to previous
uno.nsmallest(5,['population'])


# In[18]:

#Number of values of life expectancy > 85
uno[uno.life_expectancy > 85].shape[0]


# In[19]:

#All values in location that contain C
uno[uno.location.str.contains('C')]


# In[20]:

#Screening of Cambodia and Africa in location
uno[uno.location.isin(['Cambodia', 'Africa'])]


# In[21]:

#All values of location that contain A
uno[uno.location.str.contains('A')]


# In[22]:

#Value counts of life_expectancy > 80 grouped by total case
uno[uno.life_expectancy > 80].total_cases.value_counts()


# In[23]:

#Counting of life_expectancy > 80 grouped by total case
uno[(uno['life_expectancy'] > 80)].groupby(['total_cases']).count()


# In[24]:

#Using lambda function and apply to insert a new column by using conditions in life_expectancy
uno.insert(8, 'New', uno.life_expectancy.apply(lambda x: 'Old' if x > 60 else 'Young'))
uno


# In[25]:

#All dates that contain 2022
uno[uno.date.str.contains('2022')]


# In[26]:

#All '1/1/2022', '9/26/2022', '9/30/2022' in date
uno[uno.date.isin(['1/1/2022', '9/26/2022', '9/30/2022'])]


# In[27]:

#Screening out all dates > '9/26/2022'
uno[(uno.date > '9/26/2022')]


# In[28]:

#Date grouped by with population and statistical description 
uno.groupby('population').date.describe()


# In[29]:

#Population grouped by with population and statistical description 
uno.groupby('population').life_expectancy.describe()


# In[30]:

#Screening out Africa in continent and life_expectancy > 80
uno[(uno.continent == 'Africa') & (uno.life_expectancy > 80)]


# In[31]:

#Screening out Europe in continent and life_expectancy > 86
uno[(uno.continent == 'Europe') & (uno.life_expectancy > 86)]


# In[32]:

#Screening out Europe in continent and population > 8.34085540e+07 and total_cases_per_million > 100000
uno[(uno.continent == 'Europe') & (uno.population > 8.34085540e+07) & (uno.total_cases_per_million > 100000)]


# In[33]:

#Screening out Germany as location and total_cases_per_million > 20000000 and new = old
uno[(uno.location == 'Germany') & (uno.total_cases > 20000000) & (uno.New == 'Old')]


# In[34]:

#Screening out Nigeria in location and total_cases > 100000 and new = young
uno[(uno.location == 'Nigeria') & (uno.total_cases > 100000) & (uno.New == 'Young')]


# In[35]:

#All unique values in location
uno.location.unique()


# In[36]:

#Number of values of top 20 date
uno.sort_values('date', ascending = False).head(20).shape[0]


# In[37]:

#Screening out Nigeria in location and total_cases > 200000 and new = young
uno[(uno.location == 'Nigeria') & (uno.total_cases > 200000) & (uno.New == 'Young')]


# In[38]:

#Screening out North America in continent and life_expectancy > 70 and date = '9/26/2022'
uno[(uno.continent == 'North America') & (uno.life_expectancy > 70) & (uno.date == '9/26/2022')]


# In[39]:

#Screening out North America in continent and United States in location and total_cases > 40000000 and population > 300000000 and new = old
uno[(uno.continent == 'North America') & (uno.location == 'United States') & (uno.total_cases > 40000000) & (uno.population > 300000000) & (uno.New == 'Old')]


# In[40]:

##Screening out North America in continent and United States in location and date = '9/26/2022'
uno[(uno.continent == 'North America') & (uno.location == 'United States') & (uno.date == '9/26/2022')]


# In[41]:

#Screening out Oceania in continent and life_expectancy	 > 70 and date = '9/26/2022'
uno[(uno.continent == 'Oceania') & (uno.life_expectancy	 > 70) & (uno.date == '9/26/2022')]


# In[42]:

#Screening out all A's in iso_code
uno[(uno.iso_code.str.contains('A'))]


# In[43]:

#Screening out total_cases > 8000000 and life_expectancy < 25 and new = young
uno[(uno.total_cases > 8000000) & (uno.life_expectancy < 25) & (uno.New == 'Young')]


# In[44]:

#Screening out Asia in continent and life_expectancy > 84 and total_cases > 1000000
uno[(uno.continent == 'Asia') & (uno.life_expectancy > 84) & (uno.total_cases > 1000000)]


# In[45]:

#Screening out JPN in iso_code or life_expectancy > 80 or China in location or new = young or new = old and total_cases > 800000000
uno[(uno.iso_code == 'JPN') | (uno.life_expectancy > 80) | (uno.location == 'China') | (uno.New == 'Young') | (uno.New == 'Old') & (uno.total_cases > 800000000)]


# In[46]:

#Screening out Asia in continent and life_expectancy == 84.63 and Japan in location
uno[(uno.continent == 'Asia') & (uno.life_expectancy == 84.63) & (uno.location == 'Japan')]


# In[47]:

#Number of values of Asia and Africa in continent
uno[(uno.continent.isin(['Asia', 'Africa']))].shape[0]


# In[48]:

#Screening out Hong Kong and Japan in location
uno[(uno.location.isin(['Hong Kong', 'Japan']))]


# In[49]:

#Histogram plot of continent
plt.figure(figsize=(8,6))
sns.histplot(uno.continent)


# In[50]:

#Box plot of population
plt.figure(figsize=(8,6))
sns.boxplot(uno.population)


# In[51]:

#Box plot of continent against life_expectancy
plt.figure(figsize=(8,6))
sns.boxplot(data = uno, x = 'continent', y = 'life_expectancy')


# In[52]:

#Box plot of continent against population
plt.figure(figsize=(8,6))
sns.boxplot(data = uno, x = 'continent', y = 'population')


# In[53]:

#Count plot of continent
plt.figure(figsize=(8,6))
sns.countplot(uno.continent)


# In[54]:

#Count plot of new
plt.figure(figsize=(8,6))
sns.countplot(uno.New)


# In[55]:

#Density plot of life_expectancy
plt.figure(figsize=(12,8))
sns.displot(uno.life_expectancy, kind = 'kde')


# In[56]:

#Pie plot of continent
uno.continent.value_counts().plot(kind = 'pie', figsize = (8,6))


# In[57]:

#Bar plot of continent
uno.continent.value_counts().plot(kind = 'bar', figsize = (10,6))


# In[58]:

#Correlation plot of the dataset
plt.figure(figsize = (10,5))
sns.heatmap(uno.corr(), annot = True, fmt = '0.1f')


# In[ ]:




