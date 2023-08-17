#!/usr/bin/env python
# coding: utf-8

# In[3]:


def HammingDistance(x, y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist

def ApproximatePatternCount(text, pattern, d):
    count = 0
    n = len(pattern)
    for i in range(len(text)-len(pattern)+1):
        working = text[i:i+n]
        dist = HammingDistance(pattern, working)
        if dist <= d:
            count += 1
    return count

