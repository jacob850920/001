# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:45:28 2020

@author: cis-user
"""

import random
ansMax=100
ansMin=0

guessAnswer=random.randint(1,99)
guessNum=0
while guessNum != guessAnswer:
    
    print(ansMin, '< ? <',ansMax)
    guessNum=eval(input())
    
    if guessNum > ansMin and guessNum < ansMax:
        
        if guessNum > guessAnswer:
            print('再小一點')
            
            ansMax = guessNum
        elif guessNum < guessAnswer:
            print('再大一點')
           
            ansMin = guessNum
        else:
            print('賓果猜對了')
    else:
        print("超出範圍")