#!/usr/bin/env python
# coding: utf-8

# In[10]:


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


# In[11]:


graph = ConstructGraph('dataset_865643_6.txt')
path = EulerianPath(graph)
print(' '.join(path))


# In[ ]:




