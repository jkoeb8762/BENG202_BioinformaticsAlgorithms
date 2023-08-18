#!/usr/bin/env python
# coding: utf-8

# In[19]:


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
    neighborhood = set()
    suffix = pattern[1:]
    suffixNeighbors = Neighbors(suffix,d)
    nucleotides = ["A", "T", "G", "C"]
    for text in suffixNeighbors:
        if HammingDistance(suffix, text) < d:
            for i in range(len(nucleotides)):
                neighborhood.add(nucleotides[i]+text)
        else:
            neighborhood.add(pattern[0]+text)
    return neighborhood
#loop through multiple strand
def IsMotif(dna, pattern, d):
    for strand in dna:
        if ApproximatePattern(strand, pattern, d) == False:
            return False
    return True

def MotifEnumeration(dna, k, d):
    #Patterns ← an empty set
    patterns = set()
    #for each k-mer Pattern in Dna
    for strand in dna:
        #generate neighborhood of k-mer pattern differing by at most d mistmatches
        for i in range(len(strand)-k+1):
            window = strand[i:i+k]
            neighborhood = Neighbors(window, d)
            #if Pattern' appears in each string from Dna with at most d mismatches
            for word in neighborhood:
                if IsMotif(dna, word, d):
                    #add Pattern' to Patterns
                    patterns.add(word)
    return patterns

