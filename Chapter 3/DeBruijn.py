#!/usr/bin/env python
# coding: utf-8

# In[67]:


def DeBruijnGraph(k, text):
    kmers = []
    n = len(text)
    #generate kmers
    for i in range(n-k+2):
        kmers.append(text[i:i+k-1])
    graphMap = {}
    for j in range(n-k+1):
        working = kmers[j]
        new = kmers[j+1]
        if working not in graphMap:
            graphMap[working] = [new]
        else:
            graphMap[working].append(new)
    return graphMap
#print(DeBruijn(4, "AAGATTCTCTAAGA"))


# In[66]:


import io
with io.open("dataset_865639_101.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        working = line
        #print(working)
#with open("dataset_865639_101_ans.txt", "w") as f:
    graphMap = DeBruijn(12, working)
    #print(graphMap)
    for key in graphMap:
        f.write(key + ': ' + " ".join(graphMap[key]) + "\n")
    #for key, value in graphMap.items(): 
    #    f.write('%s:%s\n' % (key, value))

