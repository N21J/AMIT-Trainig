#!/usr/bin/env python
# coding: utf-8

# # SF Salaries Exercise 
# 
# 

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[6]:


sal= pd.read_csv('Salaries.csv')
sal


# ** Check the head of the DataFrame. **

# In[7]:



# sal.head() so it will genarate the first five row 
sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[8]:


##know the basic info of data

sal.info()


# **What is the average BasePay ?**

# In[14]:


# use mean to calculate the average BasePay.

sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[15]:


# use the function max to calculate the highest amount of OvertimePay in the dataset.

sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[53]:


##call the index

sal[sal 'JobTitle']== 'JOSEPH DRISCOLL'


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[51]:


sal[sal 'JobTitle']==JOSEPH DRISCOLL['Benefits']


# ** What is the name of highest paid person (including benefits)?**

# In[52]:




sal['total benefits'].max()['Benefits']


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[15]:





# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[28]:


# sum all average that generate in year[2011-2014].

sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[33]:


#num of unique job titles.
sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[18]:





# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[19]:


sal['JobTitle'].nunique()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[20]:





# In[21]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[37]:


sal(title_len) = sal['JobTitle'].apply(len)
sal.corr()


# In[23]:





# # Great Job!
