#!/usr/bin/env python
# coding: utf-8

# In[85]:


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


# In[82]:


#graph = ConstructGraph('EulerianCycle\inputs\input_1.txt')
graph = ConstructGraph('dataset_865643_2.txt')


# In[83]:


initial_node = list(graph.keys())[0]
cycle = EulerianCycle(graph, initial_node)


# In[84]:


#print(' '.join(EULERIAN_CYCLE))


# In[ ]:




