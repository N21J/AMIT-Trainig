#!/usr/bin/env python
# coding: utf-8

# # QUIZ
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[ ]:


st = 'Print only the words that start with s in this sentence'


# In[31]:


#Code here
st = 'Print only the words that start with s in this sentence'

for s in st.split():
    if s[0]=='s':
        print(s)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[14]:


# this function to get even num by use the condation (%2==0)
for num in range(0,11):
    if num %2==0:
        print(num)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[16]:


#Code Here
for num in range(1,51):
    if num  %3==0:
        print(num)
        
list1 = num       


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[ ]:


st = 'Print every word in this sentence that has an even number of letters'


# In[32]:


#Code in this cell

st = 'Print every word in this sentence that has an even number of letters'


for even in st.split():
    if len(even) % 2 == 0:
        print(' even')


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[26]:


#Code in this cell
# this function use to genearte the rang of num then use the condation below to get the requreid.

for num in range (1,101):
    if num %3==0 and num %5==0:
        print('fizzbuzz')
    elif num %5==0:
        print('buzz')
    elif num %3==0 :
        print('fizz')
    else:
        print(num)


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[ ]:


st = 'Create a list of the first letters of every word in this string'


# In[21]:


#Code in this cell


st = 'Create a list of the first letters of every word in this string'

# this function use to get the first letters of every word.

d= [letter[0] for letter in st .split()]
d


# ### Great Job!
