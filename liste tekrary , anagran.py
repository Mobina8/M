#!/usr/bin/env python
# coding: utf-8

# In[20]:


def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]

all_unique(x) #False
all_unique(y) #True


# In[26]:


from collections import Counter
def anagran(frist , secend):
    return Counter(frist) == Counter(secend)

anagran("abcd3","3acdb") #true


# In[ ]:




