#!/usr/bin/env python
# coding: utf-8

# In[16]:


def DeBruijnKmers(kmers):
    graphMap = {}
    for kmer in kmers:
        suffix = kmer[1:]
        prefix = kmer[:-1]
        if prefix not in graphMap:
            graphMap[prefix] = [suffix]
        else:
            graphMap[prefix].append(suffix)
    return graphMap


# In[20]:


import io
with io.open("dataset_865640_8.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        working = line.split()
    #print(DeBruijnKmers(working))
with open("dataset_865640_8_ans.txt", "w") as f:
    graphMap = DeBruijnKmers(working)
    for key in graphMap:
        f.write(key + ': ' + " ".join(graphMap[key]) + "\n")


# In[ ]:




