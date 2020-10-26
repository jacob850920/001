# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 08:42:17 2020

@author: cis-user
"""

from random import randint
min= 1
max= 100
answer = randint(min,max)
while True:
    guess = input('密碼介於 ' + str(min) + '-' + str(max) + ':\n>>')
    guess = int(guess)
    if guess <= min or guess >= max:
        print('請輸入 ' + str(min) + '-' + str(max) + ' 之間的整數\n')
        continue
    if guess == answer:
        print('答對了！')
        break   
    elif guess < answer:
        min = guess
    else:
        max = guess