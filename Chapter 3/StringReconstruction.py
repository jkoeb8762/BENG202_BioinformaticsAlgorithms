#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import choice
def ConstructGraph(file):
    with open(file) as f:
        graph = {}
        for line in f:
            edge = line.strip().split(': ')
            graph[edge[0]] = edge[1].split(' ')
    return graph

def EulerianCycle(graph, node):
    cycle = [node]
    while graph[node]:
        working = EulerianCycle(graph, graph[node].pop())
        cycle = cycle[:1] + working + cycle[1:]
    return cycle

#Todo: Implement recursive method. 
def EulerianPath(graph):
    diff = {}
    for key, values in graph.items():
        if key not in diff:
            diff[key] = len(values)
        else:
            diff[key] += len(values)
        for value in values:
            if value not in diff:
                diff[value] = -1
            else:
                diff[value] -= 1
    keys = [node for node, dif in diff.items() if dif == -1][0]
    values = [node for node, dif in diff.items() if dif == 1][0]
    if keys in graph:
        graph[keys].append(values)
    else:
        graph[keys] = [values]
    
    initial = list(graph)[0]
    cycle = EulerianCycle(graph,initial )
    index = 0
    while (True):
        if cycle[index] == keys and cycle[index + 1] == values:
            break
        index += 1
    return cycle[index + 1:] + cycle[1:index + 1]


# In[2]:


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
            


# In[3]:


def PathToGenome(reads):
    path = reads[0]
    for read in reads[1:]:
        n = len(read)
        path += read[n-1:]
    return path


# In[4]:


def StringReconstruction(k, pattern):
    dB = DeBruijnKmers(pattern)
    path = EulerianPath(dB)
    text = PathToGenome(path)
    return text


# In[5]:


import io
with io.open("dataset_865643_7.txt", mode="r", encoding="utf-8") as f:
    k = f.readline()
    working = f.readline().split()
    ans = StringReconstruction(k, working)
    print(ans)


# In[ ]:




