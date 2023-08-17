#!/usr/bin/env python
# coding: utf-8

# In[52]:


def ChromosomeToCycle(Chromosome):
    Nodes = [0]*(2*len(Chromosome))
    for j in range(len(Chromosome)):
        i = Chromosome[j]
        if i > 0:
            Nodes[2*j] = 2*i-1
            Nodes[2*j+1] = 2*i
        else:
            Nodes[2*j] = -2*i
            Nodes[2*j+1] = -2*i-1
    return Nodes

def ColoredEdges(P):
    Edges = list()
    for chromosome in P:
        Nodes = ChromosomeToCycle(chromosome)
        n = len(Nodes)
        for j in range(1,n,2):
            if j != n-1:
                Edges.append([Nodes[j], Nodes[j+1]])
            else:
                Edges.append([Nodes[j], Nodes[0]])
    return Edges


# In[53]:


with open("dataset_865712_7.txt") as f: 
    P = f.readline().strip()
    P = P[1:-1]
    P = P.split(')(')
    for i in range(len(P)):
        P[i] = [int(x) for x in P[i].split(' ')]
    ans = ColoredEdges(P)


# In[54]:


for element in ans:
    print("(" + str(element[0]) + ",", ''.join(map(str, element[1:])), end = "), ")


# In[ ]:




