#!/usr/bin/env python
# coding: utf-8

# In[4]:


def KSortingReversal(P,k):
    i = k
    while P[i] != k + 1 and P[i] != -(k + 1):
        i += 1
    working = []
    temp = P[k:i+1][::-1]
    for j in range(k, i+1):
        working.append(-temp[j-k])
    for x in range(len(working)):
        P[k+x] = working[x]
    return P 
        
def GreedySorting(P):
    reversals = []
    limit = 0
    for k in range(len(P)):
        while P[k] != k + 1 and limit < 10:
            P = KSortingReversal(P, k)
            reversals.append(list(P))
            limit += 1
    return reversals    


# In[31]:


x = [-3,+4,+1,+5,-2]
y = GreedySorting(x)
print(y)


# In[33]:


with open("dataset_865704_4.txt") as f: 
    line = f.readline()
    P = [int(x) for x in line.split(" ")]
    print(P)
    ans = GreedySorting(P)
    with open("output_1.txt", "w") as d:
        for res in ans:
            d.write(" ".join(["+" + str(x) if x > 0 else str(x) for x in res]))
            d.write("\n")


# In[ ]:




