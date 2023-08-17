#!/usr/bin/env python
# coding: utf-8

# In[1]:


def BreakpointCount(P):
    P = [0] + P
    P.append(max(P) + 1)
    count = 0
    n = len(P)
    for i in range(1, n):
        if P[i] != P[i - 1] + 1:
            count += 1
    return count


# In[27]:


x = [+3, +4, +5, -12, -8, -7, -6, +1, +2, +10, +9, -11, +13, +14]
BreakpointCount(x)


# In[2]:


with open("dataset_865705_6.txt") as f: 
    line = f.readline()
    P = [int(x) for x in line.split(" ")]
    ans = BreakpointCount(P)
    print(ans)
    


# In[ ]:




