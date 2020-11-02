# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:56:26 2020

@author: USER
"""
print("↓請輸入一串數字(用,號隔開)↓",end='')
list=input()
list=list.split(',')
list=[int(i) for i in list]

for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
print(list)