#!/usr/bin/env python
# coding: utf-8

# In[22]:


def matrix_helper(x, y):
    return [[0]*y for i in range(x)]

def GlobalAlignment(match_reward, mismatch_penalty, indel_penalty, seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    score = matrix_helper(n+1, m+1)
    backtrack = matrix_helper(n+1, m+1)
    for i in range(1,n+1):
        score[i][0] = -i * indel_penalty
        backtrack[i][0] = 1
    for j in range(1, m+1):
        score[0][j] = -j * indel_penalty
        backtrack[0][j] = 2
    for i in range(1,n+1):
        for j in range(1,m+1):
            if seq1[i-1] == seq2[j-1]:
                score[i][j] = max(score[i][j-1] - indel_penalty,
                                  score[i-1][j] - indel_penalty, 
                                  score[i-1][j-1] + match_reward)
            else:
                score[i][j] = max(score[i][j-1] - indel_penalty,
                                  score[i-1][j] - indel_penalty, 
                                  score[i-1][j-1] - mismatch_penalty)
            #down
            if score[i][j] == score[i-1][j] - indel_penalty:
                backtrack[i][j] = 1
            #right
            elif score[i][j] == score[i][j-1] - indel_penalty:
                backtrack[i][j] = 2
            #diagonal
            elif score[i][j] == score[i-1][j-1] - mismatch_penalty or score[i][j] == score[i-1][j-1] + match_reward:
                backtrack[i][j] = 3
    best = score[n][m]
    a1 = ''
    a2 = ''
    x = n
    y = m
    working = backtrack[x][y]
    while(working != 0):
        if working == 3:
            x -= 1
            y -= 1
            a1 = seq1[x] + a1
            a2 = seq2[y] + a2
        elif working == 2:
            y -= 1
            a1 = '-' + a1
            a2 = seq2[y] + a2
        elif working == 1:
            x -= 1
            a1 = seq1[x] + a1
            a2 = '-' + a2
        working = backtrack[x][y]
    print(best)
    print(a1)
    print(a2)
    #print ("Alignment sequence 1: " + a1)
    #print ("Alignment sequence 2: " + a2)

    return best, a1, a2


# In[23]:


import io
#with io.open("GlobalAlignment\inputs\input_8.txt") as f:
with io.open("dataset_865692_14.txt") as f:
    lines = f.read().splitlines()
    match_reward, mismatch_penalty, indel_penalty = [int(x) for x in lines[0].split()]
    #print(match_reward, mismatch_penalty, indel_penalty )
    seq1 = lines[1].strip()
    seq2 = lines[2].strip()
GlobalAlignment(match_reward, mismatch_penalty, indel_penalty, seq1, seq2)


# In[ ]:




