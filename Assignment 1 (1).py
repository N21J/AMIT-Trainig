#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[4]:


s = 'hello'
# Print out 'e' using indexing


# this function use to print 
print(s[1])


# Reverse the string 'hello' using slicing:

# In[5]:


s ='hello'
# Reverse the string using slicing

n= s[::-1]
print (n)


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[6]:


s ='hello'
# Print out the 'o'

# Method 1:

print(s[4])


# In[7]:


# Method 2:
print(s[-1])


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[8]:


# Method 1:

list1= [0,0,0]

print(list1)


# In[9]:


# Method 2:
list2 = []
# add num to list
list2.append(0)
list2.append(0)
list2.append(0)

print(list2)


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[11]:


list3 = [1,2,[3,4,'hello']]


#change hello to goodbye

list3[2][2]= 'goodbye'
print (list3)


# Sort the list below:

# In[14]:


list4 = [5,3,4,6,1]


# sort the list

list4 = sorted(list4)
print(list4)


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[15]:


d = {'simple_key':'hello'}
# Grab 'hello'

d['simple_key']


# In[16]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'

d['k1']['k2']


# In[17]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

d['k1'][0]['nest_key'][1][0]


# In[18]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello


d['k1'][2]['k2'][1]['tough'][2][0]


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[25]:


#variables
planet = 'earth'
diameter = 12742

print("the diameter of {} is {} is kilometers".format(planet, diameter)).


# ** Given this nested list, use indexing to grab the word "hello" **

# In[1]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[26]:


lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". **

# In[21]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[30]:


d['k1'][3]['tricky'][3]['target'][3]


# ### Write a Python program to swap two variables.
# 

# In[29]:


# variables

n =10
k =16
temp=0
# swap the two input value
temp =n
n = k
k= temp
print(n,k)


# ## Thanks
