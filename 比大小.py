# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:36:01 2020

@author: USER
"""
print("↓請輸入一串數字(用,號隔開)↓",end='')
list=input()
L=list.split(',')
L=[int(k) for k in L]
T = []
while len(L) > 0:
    
    for i in L:
        m= L[0]
        if i < m:
           m = i
    L.remove(m)
    T.append(m)
                 

           

