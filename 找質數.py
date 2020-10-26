# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:30:40 2020

@author: cis-user
"""
print("找出2~N的質數，請輸入N")
n=eval(input())

for i in range(2,n):
    
   
    for j in range(2,i):
     
        if i%j == 0:
            #print(n, 'is not prime')
            break
    else:
        print(i, "是質數")