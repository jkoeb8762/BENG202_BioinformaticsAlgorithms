#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = Node('')
    def insert(self, word):
        node = self.root
        for char in word: 
            if char in node.children:
                node = node.children[char]
            else:
                new = Node(char)
                node.children[char] = new
                node = new
        node.end = True


            


# In[5]:


t = Trie()
t.insert("ABC")

