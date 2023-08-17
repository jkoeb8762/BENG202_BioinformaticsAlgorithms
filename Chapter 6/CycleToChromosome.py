#!/usr/bin/env python
# coding: utf-8

# In[14]:


def CycleToChromosome(Nodes): 
    n = len(Nodes)//2
    Chromosome = [0]*n
    for j in range(n):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome[j] = int(Nodes[2*j+1]//2)
        else: 
            Chromosome[j] = int(-Nodes[2*j] // 2)
    return Chromosome


# In[6]:


x = [1,2,4,3,6,5,7,8]
CycleToChromosome(x)


# In[23]:


with open("dataset_865712_5.txt") as f: 
    line = f.readline()
    line = line.replace('(','').replace(')','')
    Cycle = [int(x) for x in line.split(" ")]
with open("CycleToChromosome_ans.txt", "w") as d:
    Chromosome = CycleToChromosome(Cycle)
    for x in Chromosome:
        d.write(" ".join(["+" + str(x) if x > 0 else str(x)]) + " ")


# In[ ]:




