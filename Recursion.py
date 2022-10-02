#!/usr/bin/env python
# coding: utf-8

# # Recursion

# A way of solving a problem by having a function calling itself

# # ** Programing the same operations multiple items with different items. \
# ** In every step we try smaller inputs to make the problems smaller. \
# ** Base condition is needed to stop the recursion, otherwise infinite loop will occur. \
# ###example

# In[5]:


def recu(num):
    if num ==1:
        print('Key Found')
    else:
        recu(num-1)
recu(10)


# # Why we need Recursion

# 1. Recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use
# ### When to choose Recursion
#     ** If you can divide the problems into similar subproblems \
#     ** Design an algorithm to compute nth \
#     ** Write code to list the n \
#     ** Implement a method to compute all \ 
#     ** Practice
# 
# 2. The prominent usage of recursion in data structures like trees and graphs.
# 3. Interviews
# 4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)

# # When to use it?
# - When we use memoization in recursion
# - When we can easily breakdown a problem into similar subproblem
# - When we are fine with extra overhead (both time and space) that comes with it
# - When we need a quick working solution instead of efficient one
# - When traverse a tree

# # When avoid it?
# - If time and space complexity matters for us.
# - Recursion uses more memory. If we use embedded memory. For example an application 
# that takes more memory in the phone is not efficient
# - Recursion can be slow

# ### Find the factorial of a number 

# In[10]:


def factorial(num):
    assert num >= 0 and int(num)==num,'The num should be Positive and an Integer'
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))
print(factorial(10))


# ### Find the Fibonacci number
# 0,1,1,2,3,5,8,13,.............

# In[14]:


def fibonacci(num):
    assert num >= 0 and int(num)==num,'The num should be Positive and an Integer'
    if num in [0,1]:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(4))
print(fibonacci(5))


# ### Find sum of postive interger number

# In[19]:


def sumOfDigit(n):
    assert n>= 0 and int(n)==n,'The num should be Positive and an Integer'   # constrint
    if n == 0:     #stoping condition
        return 0
    else:
        return (n%10)+sumOfDigit(n//10)
print(sumOfDigit(545))
print(sumOfDigit(54675))


# ### Find Power of a Integer (x^n = x^n * x^n-1)

# In[18]:


def Power(base,sep):
    assert sep >= 0 and int(sep)==sep , 'The num should be Positive '
    if sep == 0:
        return 1
    return base * Power(base,sep-1)
print(Power(5,2))
    


# ### FInd GCD (Greatest common divisor)

# In[7]:


def gcd(a,b):
    assert int(a)==a and int(b)==b,'Both a,b must be an Integer'
    if a < 0 :
        a = -1*a
    if b<0:
        b = -1*b
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(8,-16))


# ### Decimal to Binary

# In[1]:


def decimalToBinary(n):
    assert int(n)==n, 'n must be an Integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))
print(decimalToBinary(10))


# In[ ]:




