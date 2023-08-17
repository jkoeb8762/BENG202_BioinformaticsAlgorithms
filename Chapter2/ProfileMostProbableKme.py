#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Probability(pattern, profile):
    prob = 1
    for i in range(len(pattern)):
        prob *= profile[pattern[i]][i]
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

