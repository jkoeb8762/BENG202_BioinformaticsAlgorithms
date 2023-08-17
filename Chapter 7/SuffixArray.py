#!/usr/bin/env python
# coding: utf-8

# In[36]:


def SuffixArray(Text):
    n = len(Text)
    suffixarr = {i: text[i:] for i in range(n)}
    suffix_array = [x for x,_ in sorted(suffixarr.items(), key=lambda x: x[1])]
    return suffix_array


# In[38]:


#with open('SuffixArray/inputs/input_6.txt') as f: 
with open('dataset_865765_2.txt') as f:
    text = f.read().strip()
s = SuffixArray(text)
print(' '.join(str(x) for x in s))


# In[ ]:




