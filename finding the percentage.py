# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 00:05:15 2022

@author: Mugdho
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    su=  sum(student_marks[query_name])
    avg = su/3
    print('%.2f'%avg)