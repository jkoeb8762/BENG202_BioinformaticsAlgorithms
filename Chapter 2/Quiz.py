#!/usr/bin/env python
# coding: utf-8

# In[175]:


def ScatteredPatternCount(text, pattern, overlap):
    patternCount = 0
    index = []
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            patternCount +=1
            index.append(i)
    scatterCount = 1
    last = 0
    #print(index)
    for i in range(1,len(index)):
        if(index[i]-index[last]) >= len(pattern)-overlap:
            last = i
            scatterCount +=1
    return scatterCount


# In[176]:


ScatteredPatternCount('ACTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACAAGGTCACATCACATCACATCACATCACATCACATCACATCACAGCCCTCACATCACATCACATCACATCACATCACATCACACGTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACAATCTCACATCACATCACATCACATCACATCACATCACATCACACTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACACTTTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACACCCCTCACATCACATCACATCACACGCGTCACATCACATCACATCACAGTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACAGTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACAATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCTTTCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACAATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACATCACAATCACATCACATCACATCACA', 'TCACATCACATCACATCACA', 1)


# In[180]:


ScatteredPatternCount("GATATATATCATATATATATATG","ATATAT",3)


# In[178]:


text = 'GGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCCTGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCCTGCTGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGTGGTCGGTCGGTCGGTCGGCTGCAGGTCGGTCGGTCGGTCTGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCTGGGTCGGTCGGTCGGTCACGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCTGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCTGGGTCGGTCGGTCGGTCGGTCGGTCGGTCTGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCCGGGTCGGTCGGTCGGTCGGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCAGGTCGGTCGGTCGGTCCGGGTCGGTCGGTCGGTCCATGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGGTCGGTCGGTCGGTCGGTCGGTCCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCAGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCAGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCATTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCGGTCAGGTCGGTCGGTCGGTCACGGTCGGTCGGTCGGTC'


# In[181]:


Pattern = 'GGTCGGTCGGTCGGTC'
ScatteredPatternCount(text, Pattern, 3)


# In[ ]:



