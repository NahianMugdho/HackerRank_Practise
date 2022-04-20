# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:44:12 2022

@author: Mugdho
"""

n=int(input())
r = input().split()
lst=list(map(int,r))
arr = sorted(lst)
x = len(arr)
mx = max(arr)
y = -7
for i in range (0,x):
    if arr[i]<mx:
       y= arr[i]
       
       
print (y)
    
    