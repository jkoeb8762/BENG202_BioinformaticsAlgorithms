#!/usr/bin/env python
# coding: utf-8

# In[19]:


def HammingDistance(x, y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist


# In[ ]:


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

def GenerateKmers(k):
    nucleotides = ['A', 'C', 'G', 'T']
    kmers = []
    if k == 1:
        return nucleotides
    for i in GenerateKmers(k-1):
        for nucleotide in nucleotides:
            kmers.append(i + nucleotide)
    return kmers
        
def MedianString(dna, k):
    distance = float("inf")
    for kmer in GenerateKmers(k):
        dist = (DistanceBetweenPatternAndStrings(kmer, dna))
        if distance > dist:
            distance = dist
            median = kmer
    return median

