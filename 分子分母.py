# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:42:45 2020

@author: USER
"""

a = 2.0
b = 1.0
s = 0.0
for n in range(1,21):
    s  = a / b
    b,a = a , a + b
print(s)