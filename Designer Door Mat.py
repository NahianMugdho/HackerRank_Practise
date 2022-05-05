# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:10:10 2022

@author: Mugdho
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def matdesign(n,m):
    fillchar="-"
    for i in range(1,n,2):
        
        print(str('.|.'*i).center(m,'-'))
    print('WELCOME'.center(m,fillchar))
    for i in range(n-2,-1,-2):
         print(str('.|.'*i).center(m,'-'))

         
N,M=map(int,input().split())

matdesign(N,M)