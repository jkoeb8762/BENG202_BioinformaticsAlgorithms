#!/usr/bin/env python
# coding: utf-8

# In[32]:


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


# In[21]:


Chromosome = [+1, -2, -3, +4]
ChromosomeToCycle(Chromosome)


# In[34]:


with open("dataset_865712_4.txt") as f: 
    line = f.readline()
    line = line.replace('(','').replace(')','')
    Chromosome = [int(x) for x in line.split(" ")]
with open("ChromosomeToCycle_ans.txt", "w") as d:
    ans = ChromosomeToCycle(Chromosome)
    for number in ans:
        d.write(str((number)) + " ")


# In[ ]:




