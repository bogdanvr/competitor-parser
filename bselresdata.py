# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:40:22 2020

@author: office
"""
import re

with open('bs-el-res.txt', encoding='utf-8') as f:
    res = f.readlines()

res2 = []

for i in res:
    f = i.find(':', len(i) - 7)
    i = i[:f] + '#' + i[f+1:]
    res2.append(i)


regex = re.compile(':')  

for i in res2:
    y=regex.findall(i)
    if len(y) > 1:
        print(i)

len(res2)


with open('bs-el-res2.txt', 'w', encoding='utf=8') as f:
    f.writelines(res2)



    

