# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:40:20 2020

@author: cis-user
"""
#=======第一題==========
list11=[1,2,3,4,5]
list12=[6,5,4,3,2]
for i in range(0,5):
    if list11[i]>list12[i]:
              print(list11[i],end='')
    else:
              print(list12[i],end='')
#==========換行==================
print('')

#==========第二題==================

s1=[1,2,3,4,5]
s2=[6,5,4,3,2]
s3=[False,False,True,False,True]
for i in range(0,5):
    if s3[i]==True:
      print(s1[i],end='')
    else:
      print(s2[i],end='')