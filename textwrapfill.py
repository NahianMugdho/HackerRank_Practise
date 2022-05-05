# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:38:06 2022

@author: Mugdho
"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)