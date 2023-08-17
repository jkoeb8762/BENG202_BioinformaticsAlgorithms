#!/usr/bin/env python
# coding: utf-8

# In[16]:


def ReverseComplement(pattern):
    revString = pattern[::-1]
    revComp= ""
    for char in revString:
        if char == "A":
            revComp += "T"
        elif char == "T":
            revComp += "A"
        elif char == "C":
            revComp += "G"
        elif char == "G":
            revComp += "C"
    return revComp

def SharedKmers(k, seq1, seq2):
        posList = []
        seq1Dict = {}
        n = len(seq1)
        m = len(seq2)
        seq1rev = ReverseComplement(seq1)
        for i in range(n+1-k):
            s = seq1[i:i+k]
            if not s in seq1Dict:
                seq1Dict[s] = set()
            seq1Dict[s].add(i)
            s = seq1rev[i:i+k]
            if not s in seq1Dict:
                seq1Dict[s] = set()
            seq1Dict[s].add(n-i-k)
        for j in range(m+1-k):
            s = seq2[j:j+k]
            if s in seq1Dict:
                for i in seq1Dict[s]:
                    posList.append((i, j))
        return posList


# In[17]:


seq1 = "AAACTCATC"
seq2 = "TTTCAAATC"
k = 3 
SharedKmers(k, seq1, seq2)


# In[18]:


with open("dataset_865711_5.txt") as f:
    lines = f.readlines()
    k = int(lines[0].strip())
    seq1 = lines[1].strip()
    seq2 = lines[2].strip()
    #print(k, seq1, seq2)
    ans = (SharedKmers(k, seq1, seq2))
    for element in ans:
        print(element)


# In[ ]:




