# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:19:27 2020

@author: cis-user
"""

#第六題##########################################
j='Simon Peter John'
k=j.split()
l='*'
for i in range (0,3):
  print(k[i][0],end='')
  print(l*(len(k[i])-1),end=" ")
print(" ")
#第七題#################################################
word=['Company 1','Company 2','Company 3']
nword=[ ]
for i in range(0,3):
    nword.append(word[i].replace(" ","_"))
print(nword,end=" ")
print(" ")


#############################################################