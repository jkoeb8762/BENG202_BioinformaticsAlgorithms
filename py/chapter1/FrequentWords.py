#!/usr/bin/env python
# coding: utf-8

# In[3]:


def MaxMap(dict):
    maxi = max(dict.values())
    return maxi

from collections import defaultdict
def FrequencyTable1(text, k):
    #create empty dictionary
    freqMap = defaultdict(int)
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freqMap[pattern] += 1
    return freqMap

def BetterFrequentWords(text, k):
    freqPattern = []
    freqMap = FrequencyTable1(text, k)
    maximum = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == maximum:
            freqPattern.append(pattern)
    return freqPattern

