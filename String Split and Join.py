# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 02:08:41 2022

@author: Mugdho
"""

def split_and_join(line):
    # write your code here
    word=line.split()
    st = "-"
    data=[]
    for i in word:
        b = i
        data.append(b)
    return(st.join(data))
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)