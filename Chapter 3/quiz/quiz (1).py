#!/usr/bin/env python
# coding: utf-8

# In[236]:


from collections import defaultdict

def DeBruijnKmers(kmers):
    graphMap = defaultdict(list)
    for kmer in kmers:
        suffix = kmer[1:]
        prefix = kmer[:-1]
        if prefix not in graphMap:
            graphMap[prefix] = [suffix]
        else:
            graphMap[prefix].append(suffix)
    return graphMap


def EulerianCycle(graph, node):
    cycle = [node]
    try:
        while graph[node]:
            working = EulerianCycle(graph, graph[node].pop())
            cycle = cycle[:1] + working + cycle[1:]
    except:
        graph[node] = [node]
                
    return cycle


# In[115]:


import io
with io.open("quiz\input_1.txt", mode="r", encoding="utf-8") as f:
    k = f.readline()
    working = f.readline().split()


# In[240]:


db = DeBruijnKmers(working)
initial_node = list(db.keys())[4]
cycle = EulerianCycle(db, initial_node)
cycle


# In[243]:


db = DeBruijnKmers(working)
#inDegree = InDegrees(db) 
i = 0
#initial = FindInitialNode(db, inDegree)
while i < len(db):
    initial_node = list(db.keys())[i]
    print(EulerianCycle(db, initial_node))
    i += 1


# In[242]:


len(db)


# In[ ]:




