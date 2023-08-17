#!/usr/bin/env python
# coding: utf-8

# In[7]:


def HammingDistance(x, y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist

def Neighbors(pattern,d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A","C","G","T"}
    neighborhood = []
    suffix = pattern[1:]
    suffixNeighbors = Neighbors(suffix,d)
    nucleotides = ["A", "T", "G", "C"]
    for text in suffixNeighbors:
        if HammingDistance(suffix, text) < d:
            for i in range(len(nucleotides)):
                neighborhood.append(nucleotides[i]+text)
        else:
            neighborhood.append(pattern[0]+text)
    return neighborhood

