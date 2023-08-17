#!/usr/bin/env python
# coding: utf-8

# In[3]:


def HammingDistance(x, y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist

def ApproximatePatternMatching(pattern, text, d):
    pos = []
    n = len(pattern)
    for i in range(len(text)-len(pattern)+1):
        dist = HammingDistance(pattern, text[i:i+n])
        if dist <= d:
            pos.append(i)
    return pos

