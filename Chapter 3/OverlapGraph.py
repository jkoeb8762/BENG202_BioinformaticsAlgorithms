#!/usr/bin/env python
# coding: utf-8

# In[2]:


def IsOverlap(string1, string2):
    if string1[1:] == string2[:-1]:
        return True
    return False


# In[11]:


def OverlapGraph(patterns):
    n = len(patterns)
    adjList = []
    for i in range(n):
        nodes = []
        for j in range(n):
            p1 = patterns[i]
            p2 = patterns[j]
            if IsOverlap(p1, p2):
                #and p2 not in nodes:
                nodes.append(p2)
        if len(nodes) != 0:
        #and patterns[i] + ': ' + " ".join(nodes) not in adjList:
            working = patterns[i] + ': ' + " ".join(nodes)
            adjList.append(working)
    return adjList


# In[7]:


with io.open("dataset_865638_11.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        working = line.split()
with open("ok.txt", "w") as f:
    answer = OverlapGraph(working)
    for item in answer:
        f.write("%s\n" % item)

