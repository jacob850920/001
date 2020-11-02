# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:32:54 2020

@author: USER
"""
list=input()
list=list.split(',')
list=[int(i) for i in list]
for i in range(len(list)):
   
    for j in range(len(list)):
       
        if list[j] > list[i]:
           
            list[j], list[i] = list[i], list[j]
print(list)

