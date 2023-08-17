#!/usr/bin/env python
# coding: utf-8

# In[64]:


def MatrixHelper(n,m):
    return [[0]*(m) for i in range(n)]
def LongestCommonSubsequence(s,t):
    n = len(s)
    m = len(t)
    score = MatrixHelper(n+1,m+1)
    backtrack = MatrixHelper(n+1,m+1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            match = 0
            if s[i-1] == t[j-1]:
                match = 1
            score[i][j] = max(score[i][j-1], score[i-1][j], score[i-1][j-1] + match)
            #down
            if score[i][j] == score[i-1][j]:
                backtrack[i][j] = 1
            #right
            elif score[i][j] == score[i][j-1]:
                backtrack[i][j] = 2
            #diagonal
            elif score[i][j] == score[i-1][j-1] + match:
                backtrack[i][j] = 3
    return backtrack


# In[65]:


def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    working = backtrack[i][j]
    if working == 1:
        return OutputLCS(backtrack, v, i-1,j)
    elif working == 2:
        return OutputLCS(backtrack, v, i,j-1)
    else:
        return OutputLCS(backtrack, v, i-1,j-1) + v[i-1] 


# In[69]:


s1 = "AACCTTGG"
s2 = "ACACTGTGA"
backtrack = LongestCommonSubsequence(s1,s2)
ans = OutputLCS(backtrack, s1, len(s1)-1, len(s2)-1)
print(ans)


# In[72]:


import io
#with io.open("LongestCommonSubsequence\inputs\input_7.txt") as f:
with io.open("dataset_865687_5.txt") as f:
    x= f.readline().strip()
    y= f.readline().strip()
backtrack = LongestCommonSubsequence(x,y)
print(OutputLCS(backtrack, x, len(x), len(y)))

with io.open("LongestCommonSubsequence\outputs\output_7.txt") as f:
    x = f.readline().strip()
    print(x)


# In[ ]:




