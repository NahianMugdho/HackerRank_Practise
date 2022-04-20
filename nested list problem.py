# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:02:38 2022

@author: Mugdho
"""
def join(list):
    str = "\n"
    return(str.join(list))


n = int(input())
d = {}
li=[]
for i in range(n):
    keys = input() # here i have taken keys as strings
    values = float(input()) # here i have taken values as integers
    d[keys] = values


second_lowest_value = sorted(set(d.values()))[1]

for key, value in sorted(d.items()):
    if value == second_lowest_value:
        li.append(key)

li.sort()
print(join(li))