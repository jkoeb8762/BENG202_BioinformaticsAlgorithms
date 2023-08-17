#!/usr/bin/env python
# coding: utf-8

# In[78]:


#f = open('TopologicalOrdering\inputs\input_1.txt', 'r')
f = open('dataset_865696_3.txt', 'r')
line_list = f.readlines()

def ParseGraph(lines):
    graph = {}
    for line in lines:
        key, vals = line.split(': ')
        graph[int(key)] = [int(val) for val in vals.split(' ')]
    return graph

G = ParseGraph(line_list)

def DFS(graph, s, explored, distance, current_label):
    explored.add(s)
    if s in graph:
        for v in graph[s]: # for every edge (s, v)
            if v not in explored:
                DFS(graph, v, explored, distance, current_label)
    distance[current_label[0]] = s
    current_label[0] -= 1

"""Performs and outputs a topological sort of graph G using dfs
    Input: G - the input graph in the adjacency list representation via a dictionary
    distance - a dictionary representing the topological order of the vertices"""
def TopologicalSort(graph, distance):
    explored = set()
    n = len(graph)
    working = [n]
    for v in graph.keys():
        if v not in explored:
            DFS(graph, v, explored, distance, working)
            
distance = {}
TopologicalSort(G, distance)
topo = iter(sorted(distance.items()))
for _, vertex in topo:
    print(str(vertex) + "", end = " ")


# In[ ]:




