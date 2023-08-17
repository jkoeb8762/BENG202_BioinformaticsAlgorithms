#!/usr/bin/env python
# coding: utf-8

# In[9]:


def matrix_helper(x, y):
    return [[0]*y for i in range(x)]

def EditDistance(s, t):
    n = len(s)
    m = len(t)
    score = matrix_helper(n+1, m+1)
    for i in range(1,n+1):
        score[i][0] = i
    for j in range(1, m+1):
        score[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                score[i][j] = min(score[i][j-1] + 1,
                                  score[i-1][j] + 1, 
                                  score[i-1][j-1])
            else:
                score[i][j] = min(score[i][j-1] + 1,
                                  score[i-1][j] + 1, 
                                  score[i-1][j-1] + 1)
    return score[n][m]
    


# In[10]:


seq1 = "GAGA"
seq2 = "GAT"
EditDistance(seq1, seq2)


# In[12]:


import io
with io.open("dataset_865690_3.txt") as f:
    lines = f.read().splitlines()
    seq1 = lines[0].strip()
    seq2 = lines[1].strip()
    print(EditDistance(seq1,seq2))


# In[ ]:




