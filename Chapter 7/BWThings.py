#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def InverseBWT(text):
    n = len(text)
    right_col = []
    counts = {}
    for char in text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
        count = counts[char]
        working = char + str(count)
        right_col.append(working)
    left_col = sorted(right_col, key=lambda x: x[0])
    row = []
    row.append('$1')
    for i in range(n-1):
        last = row[i]
        for index, char in enumerate(right_col):
            if char == last:
                idx = index
                break
        row.append(left_col[idx])
    output = ''
    m = len(row)
    for i in range(1, m):
        output += ''.join(x for x in row[i] if not x.isdigit())
    output += '$'
    return output

with open('MultiplePatternMatching/inputs/input_4.txt') as f:
#with open('dataset_865772_4.txt') as f:
    tmp = f.read().splitlines()
    Text = tmp[0]
    pattern_list = tmp[1].split(" ")
    matches = wrapper(Text, pattern_list)
    answer = dict()
    for p in pattern_list:
        answer[p] = []
    n = len(pattern_list[0])
    for idx in matches:
        working = Text[idx:idx+n]
        if working in answer:
            answer[working].append(idx)
        else:
            answer[working] = [idx]
    file = open('output.txt', 'w')
    for key, value in answer.items():
        file.write(str(key) + ":")
        if value != []:
            file.write(' ' + ' '.join(str(x) for x in value))
        file.write('\n')
    #print(' '.join(str(pos) for pos in matches))

