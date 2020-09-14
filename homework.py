# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:00:16 2020

@author: cis-user
"""

import math
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('a,b,c只能爲數字')
    if a==0:
        return '請輸入不等於0的a值'
    else:
        d=b*b-4*a*c
        if d<0:
            return '無實根'
        elif d==0:
            x=-b/(2*a)
            return x
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            return x1,x2
#依照題目打入a,b,c
print(quadratic(1,2,1))
