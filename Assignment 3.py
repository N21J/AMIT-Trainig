#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# ### Write a function to count the number 4 in a given list.

# In[1]:


def count(my_list):
    
    counter = 0
    
    for i in my_list:
        if i ==4:
            
            counter +=1
    return  counter
l1 = [2,5,9,4,4,3,4,4,7,6]
count(l1)


# ### write a  function to check whether a number is divisible by another number.

# In[33]:


number1 = int(input('Enter the number 1:'))

number2 = int(input('Enter the number 2:'))

def check(num1,num2):
    
    if num1 % num2 ==0 :
        
        print('The {} can be divisible by {} '.format(num1 , num2))
        
    else:
        
        print('The {} can not divisible by {}'.format(num1, num2))
      
    
    
check(number1,number2)    
        
        


# ### write a function to find the maximum and minimum numbers from a sequence of numbers.

# In[24]:


def max_min( listOfNumber ):
    
    max = listOfNumber[0]
    
    min = listOfNumber[-1] 
    
    for i in listOfNumber : 
        
        # to find max
        if i > max : 
            
            max = i 
            
        # to find min
        if i < min : 
            
            min = i 
            
    print("Max is " , max)
    
    print("Min is " , min)

l1 = [1,2,3,4,5,4,4, 10 ,15 , 10 , 31]    
    
max_min(l1)


# ### Write a Python function that takes two lists and returns True if they have at least one common member.

# In[26]:


l1 = [4 , 14 , 9 , 10 , 52]
l2 = [10 , 3 ,7 ,5]

def common( list1 , list2 ):
    
    for x in list1 :
        
        if x in list2:
            
            print(" True")
common( l1 , l2)            
    


# ### Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number from the user

# In[27]:


num = int(input(' Enter number :'))

def fact(num):
    
    if num < 0:
        
        print(' The number is not correct')
        
    else :
        
        if num ==1:
            
            return 1
        
        else:
            
            return num* fact(num-1)
        
fact(num)        


# ### Write a Python function to check whether a number is in a given range.
# 
# ### The range is from 3 to 11
# 

# In[29]:


value = int(input('Enter number :'))

def ran ( valu ):
    
    for i in range (3,12):
        
        if i == valu:
            
            print(i,'in range(3,11)')
            
ran(value)            


# ### Write a  program to create the multiplication table (from 1 to 10) of a number.

# In[31]:


# function for multiplication

def multip(num):
    
    print('')
    
    print("table",num)
    
    for i in range(0,11):
        
        print(" {}*{} = ".format(num,i), num*i)
        
# for loop 1 to 10 table

for x in range(1,11):
    multip (x)


# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

# In[32]:


number1 = int(input('Enter the number1 : '))

number2 = int(input('Enter the number2 : '))

def less(num1 , num2 ):
    
    if num1 % 2 ==0 and num2 % 2 ==0:
        
        if num1 > num2:
            
            print(num2)
            
        else:
            
            print(num1)
    elif num1 % 2 != 0 or num2 % 2 !=0 :
        
        if num1 > num2:
            
            print(num1)
            
        else:
            
            print(num2)
            
less(number1 , number2)            


# In[ ]:




