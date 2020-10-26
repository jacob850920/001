# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:30:40 2020

@author: cis-user
"""
import random
ansMax=100
ansMin=0
guessCount=0
guessAnswer=random.randint(1,99)
guessNum=0
while guessNum != guessAnswer:
    #print('Guess Count=',guessCount)
    print(ansMin, '< ? <',ansMax)
    guessNum=eval(input())
    guessCount +=1
    if guessNum > ansMin and guessNum < ansMax:
        #print('guess count =',guessCount)
        #if guessNum == guessAnswer:
        #    print('bingo answer is',guessAnswer)
        #    break
        if guessNum > guessAnswer:
            print('再小一點')
            print('已猜次數',guessCount)
            ansMax = guessNum
        elif guessNum < guessAnswer:
            print('再大一點')
            print('已猜次數',guessCount)
            ansMin = guessNum
        else:
            print('賓果猜對了','總猜次數',guessCount)
    else:
        print('超出範圍')