#!/usr/bin/env python
# coding: utf-8

# In[23]:


import itertools
def KUniversalString(k):
    graph = DeBruijnKmers(BinaryStrings(k))
    intitial = list(graph)[0]
    cycle = EulerianCycle(graph, intitial)
    cycle = cycle[:-(k-1)]
    genome = cycle[0][:-1]
    for i in cycle:
        genome += i[-1]
    return genome

def EulerianCycle(graph, node):
    cycle = [node]
    while graph[node]:
        working = EulerianCycle(graph, graph[node].pop())
        cycle = cycle[:1] + working + cycle[1:]
    return cycle

def BinaryStrings(k):
    universe = ["0", "1"]
    kmers = ["".join(el) for el in itertools.product(universe, repeat=k)]
    return sorted(kmers)

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

