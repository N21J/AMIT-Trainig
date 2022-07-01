#!/usr/bin/env python
# coding: utf-8

# Dunder Methods in Python
# 
# Dunder methods are names that are and succeeded by double underscores, hence the name dunder. They are also called magic methods and can help override functionality for built-in functions for custom classes.
# 
# Why do we need Dunder methods?
# 1-str
# 
# The str method is useful when we want to use instances of our class in a print statement. As discussed earlier, it usually returns a memory object. But we can override the str method to meet our requirements.
# 
# def _str_(self):
#     s ="The current softwares and their versions are listed below: \n"
#     for key,value in self.versions.items():
#         s+= f"{key} : v{value} \n"
#     return s
# print(p)
# 
# The above str method returns the software and their versions. Ensure that the function returns a string. Below is how we would call the method.
# 
# 2-init
# 
# This is a method you must have already used if you have worked with classes. The init method is used to create an instance of the class.
# 
# def _init_(self,names):
#     if names:
#         self.names = names.copy()
#         for name in names:
#             self.versions[name] = 1
#     else:
#         raise Exception("Please Enter the names")
# 
# p = softwares(['S1','S2','S3'])
# p1 = softwares([])
# 
# The init method defined above accepts a list of names as parameters and stores it in the class’ names list. Additionally, it also populates the versions dictionary. We have also put a check on the names list.
# 
# If the list is empty, an exception is raised. Below is how we would use the init method.
# 
# The first statement would work fine but the second line would raise an exception since an empty list was passed in as a parameter.
# 
# 3-getitem
# 
# The getitem method is like the setitem method, the major difference being that the getitem method is called when we use the [] operator of a dictionary.
# 
# d = {'val':key}
# print(d['val'])
# 
# def _getitem_(self,name):
#     if name in self.versions:
#         return self.versions[name]
#     else:
#         raise Exception("Software Name doesn't exist")
# 
# print(p['S1'])
# print(p['1'])
# 
# Instances of our class can also be given a similar feature.
# 
# The above method essentially returns the version of the software. If the software is not found, it raises an exception.
# The first line would print the version of S1. But, the second line would raise an Exception since 1 doesn’t exist.
# 
# 4 -setitem
# 
# When assigning values in a dictionary, the setitem method is invoked.
# d = {}
# d['key'] = value
# 
# def _setitem_(self,name,version):
#     if name in self.versions:
#         self.versions[name] = version
#     else:
#         raise Exception("Software Name doesn't exist")
# 
# p['S1'] = 2
# p['2'] = 2
# 
# We can give instances of our class a similar feature with the help of the setitem method.
# 
# The method above is going to update the version number of the software. If the software is not found, it will raise an error.
# In the 3rd line, we use the built-in setitem method of a dictionary.
# The first line would update the version of software S1 to 2. But the second line would raise an exception since software 2 doesn’t exist.
# 
# 5-len
# 
# In a dictionary, the len method returns the number of elements in a list or the number of key-value pairs in a dictionary.
# 
# We can define a len method for our class as well.
# 
# def _len_(self):
#     return len(self.names)
# 
# print(len(p))
# 
# The len method for our class returns the number of softwares. As you might have noticed, we are using the built-in len method of a list to return the number of software.
# 
# 6-delitem
# 
# The delitem is like the setitem and getitem method. To avoid repetition, we will move on to the implementation and use case.
# 
# def _delitem_(self,name):
#     if name in self.versions:
#         del self.versions[name]
#         self.names.remove(name)
#     else:
#         raise Exception("Software Name doesn't exist")
# 
# del p['S1']
# 
# The delitem method deletes the software from the dictionary as well as the list.
# 
# 7-contains
# 
# The contains method is used when using the in operator. The return value has to be a boolean.
# def _contains_(self,name):
#     if name in self.versions:
#         return True
#     else:
#         return False
# 
# if 'S2' in p:
#     print("Software Exists")
# else:
#     print("Software DOESN'T exist")
# 
# The method checks if the name is found in the dictionary. We will be using the dictionary’s built-in contains method for that.
# The code above prints the statement inside the if blocks since software S2 is present inside the versions dictionary
# 8-add
# 
# The add method is called when using the + operator. We can define a custom add method for our class.
# 
# p1 + p2 is equal to p1.add_(p2)
# 
# def _add_(self,p2):
#     x = self.x + p2.x
#     y = self.y + p2.y
#     return point(x,y)
# p3 = p1 + p2
# 
# The above method adds the x and y coordinates of the first instance of point and the second instance of point. It will create a new instance of point and then return it.
# 
# 9- iadd
# 
# The iadd method is like the add method. It is invoked when using the += operator
# 
# def _iadd_(self,p2):
#     self.x += p2.x
#     self.y += p2.y
#     return self
# 
# p1 += p2
# print(p1)
# 
# The method above just updates an instance’s coordinates by adding the coordinates of p2. Make sure you are returning self, otherwise it will return None and won’t work as expected.
# 
# 10-call
# 
# When invoking a function like func(), we are invoking the call method.
# 
# If we put in place a call method for our class, we can do the following:
# 
# p1()
# p2()
# 
# def _call_(self):
#     print(f"Called Point {self.x},{self.y}")
# 
# 11-Other operators
# 
# _sub_(self,p2) ( - )
# _isub_(self,p2) ( -= )
# _mul_(self,p2) ( * )
# _imul_(self,p2) ( *= )
# _truediv_(self,p2)( \ )
# _itruediv_(self,p2) ( \= )
# _floordiv_(self,p2) ( \\ )
# _ifloordiv_(self,p2) ( \= )
# 

# In[2]:


class softwares:
    names = []
    versions = {}
    
    def _init_(self,names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names")
    
    def _str_(self):
        s ="The current softwares and their versions are listed below: \n"
        for key,value in self.versions.items():
            s+= f"{key} : v{value} \n"
        return s
    
    def _setitem_(self,name,version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")
    
    def _getitem_(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")
    
    def _delitem_(self,name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception("Software Name doesn't exist")
    
    def _len_(self):
        return len(self.names)
    
    def _contains_(self,name):
        if name in self.versions:
            return True
        else:
            return False


# In[3]:


class point:
    x = None
    y = None
    
    def _init_(self, x , y):
        self.x = x
        self.y = y
    
    def _str_(self):
        s = f'({self.x},{self.y})'
        return s
    
    def _add_(self,p2):
        print("In add")
        x = self.x + p2.x
        y = self.y + p2.y
        return point(x,y)
    
    def _iadd_(self,p2):
        self.x += p2.x
        self.y += p2.y
        return self
    
    def _isub_(self,p2):
        self.x -= p2.x
        self.y -= p2.y
        return self
    
    def _imul_(self,p2):
        self.x *= p2.x
        self.y *= p2.y
        return self
    
    def _itruediv_(self,p2):
        self.x /= p2.x
        self.y /= p2.y
        return self
    
    def _ifloordiv_(self,p2):
        self.x //= p2.x
        self.y //= p2.y
        return self
    
    def _call_(self):
        print(f"Called Point {self.x},{self.y}")


# *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function. Consider the following example. This is a simple function that takes two arguments and returns their sum
# 
# *args (Non-Keyword Arguments)
# **kwargs (Keyword Arguments)
# 
# 1-What is Python *args ?
# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list
# 2-What is Python **kwargs?
# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

# In[4]:


Example 1: Function to add 3 numbers

def adder(x,y,z):
    print("sum:",x+y+z)
adder(10,12,13)
sum: 35
def adder(x,y,z):
    print("sum:",x+y+z)
adder(5,10,15,20,25)

The output will be 

TypeError: adder() takes 3 positional arguments but 5 were given

Example 2: Using *args to pass the variable length arguments to the function

def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

The output will be 

Sum: 8
Sum: 22
Sum: 17

Example 3: Using **kwargs to pass the variable keyword arguments to the function 

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

The output will be 

Data type of argument: <class 'dict'>
Firstname is Sita
Lastname is Sharma
Age is 22
Phone is 1234567890

Data type of argument: <class 'dict'>
Firstname is John
Lastname is Wood
Email is johnwood@nomail.com
Country is Wakanda
Age is 25
Phone is 9876543210


#Notes:
#1-*args and **kwargs are special keyword which allows function to take variable length argument.
#2-*args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
#3-**kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
#4-*args and **kwargs make the function flexible.


# Difference between Abstraction and
# 
# ‏Abstraction in Python: Data abstraction in
# ‏ python and data encapsulation in python programming are related to each other. The main point that is necessary here to note is that data abstraction is only possible to achieve through encapsulation.
# 
# ‏Encapsulation in python: means storing or placing data in a single place to make it easily readable and compact in one place. Whereas data abstraction in python programming means to hide internal functionalities that are performing on the application using codes and to show only essential information (class attributes)
# 
# ‏Abstraction and Encapsulation in Python
# 
# 1-When we are developing any large or enterprise application. Then it’s a good practice to use the concepts of data encapsulation and data abstraction in the coding approach.
# 2-Both terms are different in meaning but indirectly related to each other.
# 3-There are two types of programming approaches, Procedural programming and Object-oriented programming.
# 4-Encapsulation and Abstraction come under an object-oriented approach which is designed for writing easy and readable codes.
# 5-Encapsulation means storing the code of each functionality in one place. While abstraction is responsible for presenting only non-sensitive information to the user by hiding the sensitive information.
# 
# Advantages of Abstraction in Python:
# 1-Abstraction helps in reducing programming efforts and reduce coding complexity.
# 2-It is used to hide unwanted details from the user.
# 3-It allows focusing on the main concept.
# 
# 
# 
#  Conclusion: Data abstraction doesn’t mean avoiding storing data, that is not necessary for some specific operation. Being a programmer, it is a good practice to define a separate method in which you can store less important data so that it can be used later when needed.

# In[ ]:


#Example elaborating the approach of data encapsulation and abstraction in Python.

class Person:
    def _init_(self):
        self.name = "Jack Matte"

    def bio(self):
        self.addr = "Bakers street, London"
        self.taxInfo = "HUAPK29971"
        self.contact = "01-777-523-342"
        print(self.addr, self.taxInfo, self.contact)

    def interest(self):
        self.favFood = "Chinese"
        self.hobbies = "Python Programming"
        self.bloodGroup = "A+"
        print(self.favFood, self.hobbies, self.bloodGroup)

obj = Person()
print(obj.name)
obj.bio()
obj.interest()

