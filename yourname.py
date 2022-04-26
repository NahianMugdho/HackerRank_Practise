# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 02:31:15 2022

@author: Mugdho
"""

def print_full_name(first, last):
    # Write your code here
    text = last+"!"
    print("Hello",first,text,"You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)