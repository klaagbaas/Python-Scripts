# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:12:54 2021

@author: Kaspar
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    nr = len(aStr)
    if nr == 0:
        return False
    elif nr == 1:
        return char == aStr
    else:
        if char == aStr[nr//2]:
            return True
        elif char < aStr[nr//2]:
            return isIn(char, aStr[:nr//2])
                        
        else:
            return isIn(char, aStr[(nr//2)+1:])

print(isIn('a', 'abc'))