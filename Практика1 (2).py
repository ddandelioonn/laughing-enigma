#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 код первой задачи
x = [8,5,6,9,7,1]
print (x[0], x[2], x[-2])
def nes (x,n):
    return x[n]


# In[1]:


#2 код второй задачи
x = [1,2,3,4,5,6,7,8,9]
def nes (x,N):
    return x[N]**N
print(nes(x,4))


# In[3]:


#3 код третьей задачи
s = 'Сургут'
k=0
for i in range (len(s)):
    if s[i] == 'у':
        k=k+1
        if k==2:
            print(i)


# In[6]:


#4 код четвертой задачи
s = '1011110000'
r = s[::-1]
k=0
for i in range (len(s)):
    if r[i] == '0':
        k=k+1
    if r[i] == '1':
        break
print(k)


# In[3]:


#5 код пятой задачи
s = input("Введите строку: ")
print(s[::-1])


# In[2]:


#6 код шестой задачи
s = [5, 5, 5, 5, 5] 
if len(set(s)) == 1:
    print('Входной массив состоит из одного и того же значения')
else:
    print('Входной массив не состоит из одного и того же значения')


# In[5]:


#7 код седьмой задачи
import re
def validate_password(password):
    if len(password) < 16:
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.match('^[a-zA-Z0-9]+$', password):
        return False
    return True
password = input("Введите пароль: ")
if validate_password(password):
    print("Пароль надежный")
else:
    print("Пароль ненадежный, придумайте другой")


# In[7]:


#8 код восьмой задачи
l= [[2, 4, 2], [23], [94, 3, [66]], 3]  
def flatten(x):
    a = []
    for i in x:
        if isinstance(i, list):
            a.extend(flatten(i))
        else:
            a.append(i)
    return a
print(flatten(l))


# In[10]:


#9 код девятой задачи
dict = {'a': 5, 'b': 2, 'c': 9, 'd': 4}
def max_k(x):
    a = -999999
    k = 0
    for i in x:
        if x[i] > a:
            a = x[i]
            k = i
    return k
print(max_k(dict))


# In[16]:


#10 код десятой задачи
X = [1, 4, 3, 6, 4, 5, 5, 6]
def not_unique(X):
    a = []
    for i in X:
        if X.count(i) > 1 and i not in a:
            a.append(i)
    return a
print(not_unique(X))


# In[ ]:




