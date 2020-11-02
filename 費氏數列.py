# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:25:30 2020

@author: USER
"""
# 利用數學家歸納的公式解
# F(n)= sqrt_5/5 * (((1+sqrt_5)/2)**n - ((1-sqrt_5)/2)**n)

from decimal import *
getcontext().prec = 6000
print("↓f(n),請輸入n=?↓",end='')
n = int(input())-1

sqrt_5 = Decimal(5).sqrt()
x=sqrt_5/5 * (((1+sqrt_5)/2)**n - ((1-sqrt_5)/2)**n)
print("公式解的答案為：")   
print(f"{x:.0f}")


# 驗證用，非遞迴解法
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n>1:

        prev = 1    #第n-1項的值
        p_prev = 0  #第n-2項的值
        result = 1  #第n項的值

        for i in range(1,n):
           result = prev+p_prev 
           p_prev = prev
           prev = result
        return result
print("驗證的答案為：")    
print(f(n))
