#!/usr/bin/env python
# coding: utf-8

# In[5]:


#usiong the sample numbers series in form of tuple 

#defining the odd_numbers as 0 and even_numbers as 0 initially

#using for loop for iteration and using a as another object ,in membership operator is used for getting the value of a from numbers

#then assignment operator even_numbers+=1 is used for count the even numbers and add till loop ends 

#then assignment operator odd_numbers+=1 is used for count the odd numbers and add till loop ends 

#print statement is used for even and odd numbers

numbers=(1,2,3,4,5,6,7,8,9)
odd_numbers=0
even_numbers=0
for a in numbers:
    if not a%2:
        even_numbers+=1
    else:
        odd_numbers+=1
print("Numbers of even numbers :" , even_numbers)
print("Numbers of odd numbers :" , odd_numbers)


# In[ ]:




