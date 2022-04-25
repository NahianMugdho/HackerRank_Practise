# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 02:17:58 2022

@author: Mugdho
"""
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    
    print(hash(integer_list))