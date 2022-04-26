# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:54:46 2022

@author: Mugdho
"""

def mutate_string( string,  position, character):
    st=list(string)
   
    sr = ""
    
    for i in st:
        st[position]=character
    return (sr.join(st))   

        
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)