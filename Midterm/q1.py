#!/usr/bin/env python
# coding: utf-8

# In[32]:


def Probability(pattern, profile):
    prob = 1
    for i in range(len(pattern)):
        working = float(profile[pattern[i]][i])
        prob *= working
    return prob

def ProfileMostProbableKmer(text, k, profile):
    bestScore = 0
    mostProbable = ''
    for i in range(len(text)-k+1):
        working = text[i:i+k]
        score = Probability(working, profile)
        if score > bestScore:
            bestScore = score
            mostProbable = working
    return mostProbable


def ScatteredPatternCount(text, pattern, overlap):
    patternCount = 0
    index = []
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            patternCount +=1
            index.append(i)
    scatterCount = 1
    last = 0
    #print(index)
    for i in range(1,len(index)):
        if(index[i]-index[last]) >= len(pattern)-overlap:
            last = i
            scatterCount +=1
    return scatterCount


# In[87]:


#Code inspired by three functions above- modifying ProfileMostProbableKmer to store indexes of the kmers instead, and taking inspiration from ScatteredPatternCount to count. 
def q1(text, k, profile, threshold, d):
    idxs = []
    for i in range(len(text)-k+1):
        working = text[i:i+k]
        score = Probability(working, profile)
        if score > threshold:
            idxs.append(i)
    print(idxs)
    if idxs:
        count = 1
    else: 
        count = 0
    bestCount = count
    for i in range(1, len(idxs)):
        if idxs[i] - idxs[i-1] <= d:
            count += 1
        else:
            count = 0 
        if count >= bestCount:
            bestCount = count
            
    return bestCount


# In[89]:


#with open("input_1.txt") as f: 
with open("dataset_901302_2.txt") as f:
    lines = f.read().strip().splitlines()
    seq = lines[0]
    k = int(lines[1])
    profile = {}
    nucleotides = ["A", "C", "G", "T"]
    for i in range(len(nucleotides)):
        working = nucleotides[i]
        profile[working] = lines[i+2].split()
    threshold = float(lines[6])
    d = int(lines[7])
    print(d)
    #print(seq, k, profile, threshold, d)
    print(q1(seq, k, profile, threshold, d))

