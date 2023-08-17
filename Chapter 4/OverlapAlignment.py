#!/usr/bin/env python
# coding: utf-8

# In[7]:


def matrix_helper(x, y):
    return [[0]*y for i in range(x)]

def OverlapAlignment(match_reward, mismatch_penalty, indel_penalty, seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    score = [[0 for j in range(m)] for i in range(n)]
    backtrack = [[0 for j in range(m)] for i in range(n)]
    optimal = (0,0)
    for i in range(1,n):
        for j in range(1,m):
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
                
    x = n - 1
    y = max(range(m), key=lambda x: score[i][x])
    a1 = ""
    a2 = ""
    maxi = score[i][j]
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
    return maxi, a1, a2

