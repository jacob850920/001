# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:14:06 2020

@author: USER
"""

import random
ansMax=100
ansMin=0
guessCount=0
guessAnswer=random.randint(1,99)
guessNum=0
while guessNum != guessAnswer:
    
    print(ansMin, '< ? <',ansMax,end='')
    guessNum=eval(input())
    guessCount +=1
    if guessNum > ansMin and guessNum < ansMax:
       
        if guessNum > guessAnswer:
            print('再小一點')
            print('已猜次數',guessCount,'\n')
            ansMax = guessNum
        elif guessNum < guessAnswer:
            print('再大一點')
            print('已猜次數',guessCount,'\n')
            ansMin = guessNum
        else:
            print('賓果猜對了',guessCount,'\n')
    else:
        
        print('超出範圍')
        print('已猜次數',guessCount,'\n')