# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:26:46 2020

@author: sajal
"""
'''dice simulator'''
import random
import time

user_inp = 'yes'

while user_inp == 'yes' or user_inp == 'y':
    
    print('dice is rolling...')
    time.sleep(1)
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print('dice-1 value is: ',dice1)
    print('dice-2 value is: ',dice2)
    
    time.sleep(1)
    
    if dice1 == dice2:
        print('congo you won!!..')
        
    user_inp = input('do you want to play again(y/n):- ').lower()
time.sleep(1)
print('thank you for playing...😊😊')

