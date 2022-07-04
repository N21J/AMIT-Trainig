#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# 

# #### Import NumPy as np

# In[2]:


import numpy as np


# #### Create an array of 10 zeros 

# In[3]:


#array of 10 zeros
np.zeros(10)


# #### Create an array of 10 ones

# In[4]:


#array of 10 ones
np.ones(10)


# #### Create an array of 10 fives

# In[18]:


x =np.arange(0 ,11)

x[0:11] = 5

x


        


# #### Create an array of the integers from 10 to 50

# In[24]:


#array of the integers from 10 to 50

np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[25]:


# array of all the even integers from 10 to 50
np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[32]:


#3x3 matrix with values ranging from 0 to 8
np.arange(0,9).reshape((3,3))


# #### Create a 3x3 identity matrix

# In[33]:


#identity matrix
np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[34]:


#generate a random number between 0 and 1
np.random.randint(0,1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[36]:


#give random number accorde to standard normal distribution[0:1]

np.random.randn(25)


# #### Create the following matrix:

# In[42]:


np.arange(0,1,0.01)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[44]:


# generate matrix start with 0 end with 1 divide to 20 part

np.linspace( 0 , 1 , 20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[46]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[47]:


# get the value after the value after row number 2 and the value after first col.

mat[2: , 1: ]


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[48]:


mat[ 3,4 ]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[49]:



mat[0:3 , 1:2]


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[50]:


#get the value in row 4.

mat[4]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[51]:


# get the all row after the row number 3.

mat[3:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[52]:


#This function use to get the sum of all the values in mat array.
mat.sum()


# #### Get the standard deviation of the values in mat

# In[53]:


#This function use to get standard deviation of the values in mat array.


mat.std()


# #### Get the sum of all the columns in mat

# In[54]:


# This function use to get sum of all col in mat array.


mat.sum(axis=1)


# # Great Job!
