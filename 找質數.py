# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:30:40 2020

@author: cis-user
"""
print("↓請輸入n，找出2~n的質數↓",end='')
n=eval(input())
for i in range(2,n):
    for j in range(2,i):
     
        if i%j == 0:
            break
    else:
        print(i, '是質數')