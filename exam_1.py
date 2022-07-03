#!/usr/bin/env python
# coding: utf-8

# # Exam1
# 
# 

# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

# In[9]:


number1 = int(input("Enter The number 1 : "))

number2 = int(input("Enter The number 2 : "))
    
def lesser_of_two_evens(num1 , num2 ) : 
    
    if num1 % 2 == 0 and num2 % 2 == 0 :
        
        if num1 > num2 : 
            
            print(num2)
            
        else : 
            
            print(num1)
            
    elif num1 % 2 != 0 or num2 % 2 != 0 :
        
        if num1 > num2 : 
            
            print(num1)
            
        else : 
            
            print(num2)
            
lesser_of_two_evens(number1 , number2 )            


# In[ ]:


# Check
lesser_of_two_evens(2,4)


# In[10]:


# Check
lesser_of_two_evens(2,5)


# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False

# In[20]:


def animal_crackers(text):
    
    # this function will compare between the first letter in s1 and s2 then will print true if it is same and false if it wrong.
    s1 , s2 = text.split(' ')
    print( s1[0].upper() == s2[0].upper())
    


# In[21]:


# Check
animal_crackers('Levelheaded Llama') # the first letter in both word was the same so that will print true.


# In[22]:


# Check
animal_crackers('Crazy Kangaroo')#the first letter in both word was the differint so that will print false.


# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# 
#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

# In[33]:


def makes_twenty(n1,n2):
   # this function will print true if sum of two int is 20.


    if n1 + n2 == 20 :
        
        print('true')
        
        
 #this function will print true if n1 is 20 or n2 = 20.

    elif n1 == 20 or n2 ==20:
        
        print('true')
        
#will print false if the n1 or n2 not equle 20 and if sum of two num not equle 20.        
    else:
        print('false')


# In[34]:


# Check
makes_twenty(20,10)


# In[35]:


# Check
makes_twenty(2,3)


# #### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#      
#     old_macdonald('macdonald') --> MacDonald
#     
# Note: `'macdonald'.capitalize()` returns `'Macdonald'`

# In[44]:


def old_macdonald(name):
    letters = list(name)
    
    for index in range(len(name)):
        
        if index == 0:
            
            letters[index] = letters[index].upper()
        
        elif index ==3:
            
            letters[index] = letters[index].upper()
            
    return "".join(letters)        
    


# In[45]:


# Check
old_macdonald('macdonald')


# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
#     
# NOTE: `abs(num)` returns the absolute value of a number

# In[46]:


def almost_there(n):
   # if n =90 and <= 110 return true or n=190 and <=210 return true , else return false. 
    return 90 <= n <=110 or 190 <=n <=210
    


# In[47]:


# Check
almost_there(104)


# In[48]:


# Check
almost_there(150)


# In[49]:


# Check
almost_there(209)


# #### FIND 33: 
# 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# 
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

# In[54]:


def has_33(nums):
    
    
    for x in nums : 
        
        if x in nums : 
            
            print("True")

         


# In[55]:


# Check
has_33([1, 3, 3])


# In[56]:


# Check
has_33([1, 3, 1, 3])


# In[57]:


# Check
has_33([3, 1, 3])


# #### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#     paper_doll('Hello') --> 'HHHeeellllllooo'
#     paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# In[82]:


def paper_doll(text):
    
    for letters in text:
        
        newtext= str(text*3)
        
        
        print(newtext)
        
  


# In[83]:


# Check
paper_doll('Hello')


# In[74]:


# Check
paper_doll('Mississippi')


# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

# In[85]:


def blackjack(a,b,c):
    
    
    for n in range(1,12):
        
        if n1+n2 <== 21:
            
            print(n1+n2)
        elif n1+n2 > 21 and there is 11:
            
            print(n1+n2 -10)
            
        else:
            return 'BUST'


# In[ ]:


# Check
blackjack(5,6,7)


# In[ ]:


# Check
blackjack(9,9,9)


# In[ ]:


# Check
blackjack(9,9,11)


# #### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#  
#     summer_69([1, 3, 5]) --> 9
#     summer_69([4, 5, 6, 7, 8, 9]) --> 9
#     summer_69([2, 1, 6, 9, 11]) --> 14

# In[ ]:


def summer_69(arr):
    pass


# In[ ]:


# Check
summer_69([1, 3, 5])


# In[ ]:


# Check
summer_69([4, 5, 6, 7, 8, 9])


# In[ ]:


# Check
summer_69([2, 1, 6, 9, 11])


# #### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# 
#      spy_game([1,2,4,0,0,7,5]) --> True
#      spy_game([1,0,2,4,0,5,7]) --> True
#      spy_game([1,7,2,0,4,5,0]) --> False
# 

# In[ ]:


def spy_game(nums):
    pass


# In[ ]:


# Check
spy_game([1,2,4,0,0,7,5])


# In[ ]:


# Check
spy_game([1,0,2,4,0,5,7])


# In[ ]:


# Check
spy_game([1,7,2,0,4,5,0])


# #### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#     count_primes(100) --> 25
# 
# By convention, 0 and 1 are not prime.

# In[ ]:


def count_primes(num):
    pass
                


# In[ ]:


# Check
count_primes(100)


# ## Great Job!
