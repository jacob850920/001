# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:19:27 2020

@author: cis-user
"""

#第六題(自己想的沒for版本)##########################################
j="Simon Peter John"
k=j.split(' ')
k1=k[0]
k2=k[1]
k3=k[2]
l1=k1[0][0]
l2=k2[0][0]
l3=k3[0][0]
h1=len(k1)-1
h2=len(k2)-1
h3=len(k3)-1
print(l1+"*"*h1+' '+l2+'*'*h2+' '+l3+'*'*h3)
#第六題(有for版本)########################################
v="Simon Peter John"
z=v.split(' ')
z1=z[0]
z2=z[1]
z3=z[2]
b1=z1[0][0]
b2=z2[0][0]
b3=z3[0][0]
a1=["*"for i in z1[1:]]
a1="".join(a1)
a2=["*"for i in z2[1:]]
a2="".join(a2)
a3=["*"for i in z3[1:]]
a3="".join(a3)
y=[]
y.append(b1+a1)
y.append(b2+a2)
y.append(b3+a3)
print(y)
#第七題#################################################
word=['Company 1','Company 2','Company 3']
word1=word[0]
word10=word1.replace(" ", "_")
word2=word[1]
word20=word2.replace(" ", "_")
word3=word[2]
word30=word3.replace(" ", "_")
nword=[]
nword.append(word10)
nword.append(word20)
nword.append(word30)
print(nword)
#第八題######################################################
list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    list2.append(str(i)+"$")
print(list2)
#第九題#####################################################
list3=[]
for i in list2:
    list3.append(str(i).replace("$", ""))
print(list3)
#第十題#####################################################
list1=[1,2,3,4]
list2=[5,6,7,8]
print(list(zip(list1,list2)))
##第1題####################################################
s='I love you and you love him and who loves who'
a=s.split(' ')
print(a)
###########################################################
print(set(s))
keys=(set(s))
values=[0 for i in keys]
dictionary={keys:values for keys, values in zip(keys,values)}
print(dictionary)
for i in s:
    dictionary[i]+=1
print(dictionary)
#############################################################