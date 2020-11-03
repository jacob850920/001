# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:25:13 2020

@author: USER
"""

#### 第一題.找質數======================================
# print("請輸入n，找出2~n的質數",end="")
# n=eval(input())
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j ==0:
#             break
#     else:
#             print(i,"是質數")      

#### 第二題.排大小======================================  
# print("請輸入一串數字(用,隔開)",end='')
# list1=input()
# L=list1.split(',')
# L=[int(k) for k in L]
# T=[]
# while len(L)>0:
#     m=L[0]
#     for i in L:
#         if i<m:
#             m=i
#     L.remove(m)
#     T.append(m)
# print(T) 

#### 第三題.分數序列======================================
# a=2.0
# b=1.0
# s=0.0
# ts=[]
# n=int(input(",前n項之和請輸入n")) 
# for n in range(0,n):
#     s=a/b
#     b,a=a,a+b
#     ts.append(s)
# print(sum(ts))    

#### 第四題.質因數分解======================================           
# print("請輸入需要質因數分解的數",end='')
# num=eval(input())
# it=[]
# print(num,"=",end='')
# while num !=1:
#     for i in range(2,int(num+1)):
#         if num%i==0:
#             it.append(i)
#             num=num/i
#             break
# for i in range(0,len(it)-1):
#         print(it[i],'*',end='')
# print(it[-1])    


#### 第五題.50次反彈====================================== 
# h=int(input("請輸入起始高度(米):"))
# N=50
# M=[]
# height=[]
# for i in range(1,N+1):
#     if i ==1:
#         M.append(h)
#     else:
#         M.append(2*h)
#     h=h/2
#     height.append(h)
# s=sum(M)
# u=height[-1]
# print("總經過路成為：%f"%(s))
# print("第50次反彈高度為:%f"%(u))

### 第六題.費氏數列======================================
###利用數學家歸納的公式解
###F(n)=sqrt_5/5*((1+sqrt_5/2)**n-((1-sqrt_5)/2)**n)
# from decimal import *
# getcontext().prec=6000 #用於計算根號5，避免不精準問題
# import time
# tStart = time.process_time() #用於計算執行時間
# print("f(n),請輸入n=?",end='')
# n=int(input())+1
# sqrt_5=Decimal(5).sqrt()
# x=sqrt_5/5*(((1+sqrt_5)/2)**n-((1-sqrt_5)/2)**n)


# print(f"{x:.0f}")
# tEnd = time.process_time()
# print("執行時間為:%f秒"%(tEnd-tStart))            

#### 第七題.終極密碼戰======================================
# import random
# gmax=100
# gmin=0
# n=0
# ans=random.randint(1, 99)
# num=0
# while num!=ans:
#     print(gmin,'<?<',gmax,end='')
#     num=eval(input())
#     n=n+1
#     if num>gmin and num<gmax:
        
#         if num>ans:
#             print("再小一點")
#             print("已猜次數",n,'\n')
#             gmax=num
#         elif num<ans:
#            print("再大一點")
#            print("已猜次數",n,'\n')
#            gmin=num
#         else:
#             print("猜對啦")
#             print("總猜次數",n,'\n')
#             break
#     else:
#         print("超出範圍")
#         print("已猜次數",n,'\n')        
        
        