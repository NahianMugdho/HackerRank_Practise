# -*- coding: utf-8 -*-
"""
Created on Thu May  5 02:19:43 2022

@author: Mugdho
"""

s = input()

print (any([i.isalnum() for i in s]))
print (any([i.isalpha() for i in s]))
print (any([i.isdigit() for i in s]))
print (any([i.islower() for i in s]))
print (any([i.isupper() for i in s]))