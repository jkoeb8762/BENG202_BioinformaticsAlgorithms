#!/usr/bin/env python
# coding: utf-8

# In[74]:


def MatrixHelper(n,m):
    return [[0]*(m+1) for i in range(n+1)]

def LongestPathLength(n, m, down, right):
    score = MatrixHelper(n, m)
    for i in range(1, n+1):
        score[i][0] = score[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        score[0][j] = score[0][j-1] + right[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            score[i][j] = max(score[i-1][j] + down[i-1][j],
                              score[i][j-1] + right[i][j-1])
    return score[n][m]


# In[75]:


import io
#with io.open("LongestPathLength\inputs\input_5.txt") as f:
with io.open("dataset_865685_10.txt") as f:
    lines = f.read().splitlines()
    n, m = [int(x) for x in lines[0].split()]
    #print (n)
    #print(m)
    down = []
    right = []
    for i in range(1,n+1):
        down.append([int(x) for x in lines[i].split()])
    #print(down)
    for j in range(n+2, len(lines)):
        right.append([int(x) for x in lines[j].split()])
    #print(right)
    print(LongestPathLength(n,m,down,right))


# In[ ]:




