#!/usr/bin/env python
# coding: utf-8

# In[2]:


#declare a array
a = [1,2,3,4,5]
b = []
print(a)
print(b)


# In[5]:


print(a[len(a)-1])


# In[7]:


import array as arr


# In[8]:


arr1 = arr.array('i',[1,2,3,4,5])


# In[13]:


for i in range(0,len(arr1)):
    print(arr1[i],end=' ')


# In[16]:


print(arr1[len(arr1)-1])


# In[24]:


# adding values to list
a = arr.array('i',[3,4,5,6,7,8,9,10])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
a.append(11)
for i in range(len(a)):
    print(a[i],end=' ')
    


# In[28]:


# updating values to list
a = arr.array('i',[3,4,5,6,7,8,9,10])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
#value at specific ind w/o appending
a[0] = 2
for i in range(len(a)):
    print(a[i],end=' ')
print()
#value at specific ind with appending
a.insert(4,8)
for i in range(len(a)):
    print(a[i],end=' ')


# In[29]:


# deleteing values to list
a = arr.array('i',[3,4,5,6,7,8,9,10])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
a.pop(4)
for i in range(len(a)):
    print(a[i],end=' ')


# In[30]:


# remove values to list
a = arr.array('i',[3,4,5,6,7,8,9,10])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
a.remove(4)
for i in range(len(a)):
    print(a[i],end=' ')


# In[38]:


# slice an array
a = arr.array('i',[3,4,5,6,7,8,9,10])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
b = a[2:5]
for i in range(len(b)):
    print(b[i],end=' ')


# In[40]:


#searching in array
a = arr.array('i',[3,4,5,6,7,8,9,10])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
print(a.index(9))


# In[44]:


#sorting in array
a = arr.array('i',[3,4,23,5,11,6,7,8,2,9,10,6])
print(len(a))
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
a = a.tolist()
# asc order
a.sort()
#print the array
for i in range(len(a)):
    print(a[i],end=' ')
print()
# asc order
a.sort(reverse=True)
#print the array
for i in range(len(a)):
    print(a[i],end=' ')


# In[45]:


import numpy as np


# In[52]:


#1d array
a = np.array([1,2,3,4,5,6,7,8])
print(a)
print('1d')
#2d array
a = np.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]])
print(a)
print('2d')
#3d array
a = np.array([[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]],[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]])
print(a)
print('3d')
#nd array
a = np.array([[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]],[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]],ndmin=6)
print(a)
print('6d')


# In[ ]:




