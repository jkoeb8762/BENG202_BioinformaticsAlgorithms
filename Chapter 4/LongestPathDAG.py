#!/usr/bin/env python
# coding: utf-8

# In[31]:


def LongestPathDAG(start, end, graph):
    distance = [0 for _ in range(end+1)]
    backtrack = [0 for _ in range(end+1)]
    for i in range(1, end+1):
        for (source, weight) in graph[i]:
            working = distance[source] + weight
            if working >= distance[i]:
                distance[i] = working
                backtrack[i] = source
    path = []
    current = end
    while current != start:
        path.append(current)
        current = backtrack[current]
    path.append(start)
    path.reverse()
    return path


filepath = "dataset_865687_7.txt"
with open(filepath) as f:
        lines = f.read().splitlines()
        start, end = [int(x) for x in lines[0].split()]
        reverse = {k:[] for k in range(end+1)}
        for line in lines[1:]:
            source, target, weight = [int(x) for x in line.split()]
            reverse[target].append((source, weight))


# In[32]:


print(*LongestPathDAG(start, end, reverse))


# In[ ]:




