#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def HammingDistance(x, y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist

def DistanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        hammingdistance = float("inf")
        for i in range(len(string)-k+1):
            window = string[i:i+k]
            dist = HammingDistance(pattern, window)
            if hammingdistance > dist:
                hammingdistance = dist
        distance += hammingdistance
    return distance

