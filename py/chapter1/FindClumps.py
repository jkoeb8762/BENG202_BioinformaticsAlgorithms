#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import defaultdict
def FrequencyTable1(text, k):
    #create empty dictionary
    freqMap = defaultdict(int)
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freqMap[pattern] += 1
    return freqMap

def FindClumps(text, k, L, t):
    patterns = set()
    n = len(text)
    window = text[0:L]
    for i in range(n-L):
        window = text[i:i+L]
        freqMap = FrequencyTable1(window, k)
        for key in freqMap:
            if freqMap[key] >= t:
                patterns.add(key)
    return patterns

