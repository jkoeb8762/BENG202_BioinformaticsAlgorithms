#!/usr/bin/env python
# coding: utf-8

# In[5]:


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

def FrequentWordsWithMismatches(text, k, d):
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n-k):
        pattern = text[i:i+k]
        neighborhood = Neighbors(pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1
    m = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns

