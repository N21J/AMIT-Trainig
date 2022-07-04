#!/usr/bin/env python
# coding: utf-8

# ## Write a Numpy program to compute the multiplication of two given matrixes

# In[24]:


import numpy as np


# In[57]:


# create two matrix


mat1 = [[1, 0], [0, 1]]

mat2 = [[1, 2], [3, 4]]

#the two matrix
mat1
mat2

# the multiplication of two given matrixes
mat3 = np.dot(mat1, mat2)

#the result of multiplication
mat3


# ## Write a NumPy program to compute the determinant of a given square array

# In[ ]:


import numpy as np
from numpy import linalg


# In[47]:



# Creating a 2X2 matrix

mat = np.array([[1, 0], [3, 6]])
mat

# Output

print(np.linalg.det(mat))


# ## Write a NumPy program to compute the cross product of two given vectors

# In[ ]:


import numpy as np


# In[48]:


# create two matrix

mat1 = [[1, 0], [0, 1]]

mat2 = [[1, 2], [3, 4]]

#the two matrix
mat1
mat2

# cross product of two given vectors

result1 = np.cross(mat1, mat2)

result2 = np.cross(mat2, mat1)

# result of cross product
result1
result2


# ## Write a NumPy program to compute the condition number of a given matrix

# In[51]:


import numpy as np
from numpy import linalg as LA


# In[53]:


# create matrix
a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
#the matrix
a

#calculate the condition number
LA.cond(a)


# ## Write a NumPy program to compute the inverse of a given matrix

# In[ ]:


import numpy as n


# In[55]:


# create matrix

mat = np.array([[1,2],[3,4]])
#the matrix
mat

# get the inverse of matrix

result =  np.linalg.inv(mat)

result


# In[ ]:




