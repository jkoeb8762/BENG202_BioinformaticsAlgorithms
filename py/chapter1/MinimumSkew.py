#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Skew(genome):
    skew = [0]
    n = len(genome)
    for i in range(n):
        val = skew[i]
        if genome[i] == "C":
            val = skew[i]-1
        elif genome[i] == "G":
            val = skew[i]+1
        skew.append(val)
    return skew

def MinimumSkew(genome):
    pos = []
    skew = Skew(genome)
    minimum = min(skew)
    for i in range(len(genome)):
        if skew[i] == minimum:
            pos.append(i)
    return pos

