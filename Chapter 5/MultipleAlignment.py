#!/usr/bin/env python
# coding: utf-8

# In[201]:


def matrix_helper(x, y):
    return [[0]*y for i in range(x)]
def AffineAlignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    lower = matrix_helper(n+1, m+1)
    middle = matrix_helper(n+1, m+1)
    upper = matrix_helper(n+1, m+1)
    backtrack = matrix_helper(n+1, m+1)
    
    for i in range(1, n+1):
        lower[i][0] = -gap_opening_penalty - gap_extension_penalty * (i-1)
        middle[i][0] = -gap_opening_penalty - gap_extension_penalty * (i-1)
        upper[i][0] = -10*gap_extension_penalty
    for j in range(1, m+1):
        lower[0][j] = -10*gap_extension_penalty
        middle[0][j] = -gap_opening_penalty - gap_extension_penalty * (j-1)
        upper[0][j] = -gap_opening_penalty - gap_extension_penalty * (j-1)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            lower[i][j] = max(lower[i-1][j] - gap_extension_penalty, middle[i-1][j] - gap_opening_penalty)
            upper[i][j] = max(upper[i][j-1] - gap_extension_penalty, middle[i][j-1] - gap_opening_penalty)
            
            if seq1[i-1] == seq2[j-1]:
                diag = middle[i - 1][j - 1] + match_reward
            else: 
                diag = middle[i - 1][j - 1] - mismatch_penalty
            middle_scores = [lower[i][j], diag, upper[i][j]]
            middle[i][j] = max(middle_scores)
            
            backtrack[i][j] = middle_scores.index(middle[i][j]) + 1
    best = middle[n][m]
    a1 = seq1
    a2 = seq2
    x = n
    y = m     
    working = backtrack[x][y]
    while x*y != 0:
        if working == 1:
            #print(a2[y:])
            x -= 1
            #a2 = a2 + '-'
            a2 = a2[:y] + '-' + a2[y:] 
        elif working == 2: 
            x -= 1
            y -= 1
            #a1 = seq1[x] + a1
            #a2 = seq2[y] + a2
        elif working == 3:
            y -= 1
            a1 = a1[:x] + '-' + a1[x:]
        working = backtrack[x][y]
    
    for i in range(x):
        a2 = '-' + a2
    for j in range(y):
        a1 = '-' + a1
    
    return best, a1, a2


# In[197]:


seq1 = "GA"
seq2 = "GTTA"
AffineAlignment(1,3,2,1, seq1,seq2)


# In[202]:


import io
with open("AffineAlignment\inputs\input_7.txt") as f:
#with open("dataset_865691_8.txt") as f:    
    lines = f.read().splitlines()
    match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty = [int(x) for x in lines[0].split()]
    seq1 = lines[1].strip()
    seq2 = lines[2].strip()
    print(AffineAlignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, seq1,seq2))


# In[203]:


with open("AffineAlignment\outputs\output_7.txt") as f:
    lines = f.read().splitlines()
    score = lines[0]
    seq1 = lines[1].strip()
    seq2 = lines[2].strip()
    print(score, seq1,seq2)


# In[ ]:




