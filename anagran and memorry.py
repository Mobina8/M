#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import Counter
def anagran(first,second):
    import sys
    print (sys.getsizeof(first,second))# 24
    return Counter(first) == Counter(second)
anagran("abcde","badec") #True


# In[ ]:




