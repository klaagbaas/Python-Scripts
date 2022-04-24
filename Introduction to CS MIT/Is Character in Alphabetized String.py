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
    stringlength = len(aStr)
    if stringlength == 0: # no length indicates string is empty
        return False
    elif stringlength == 1: # only one character in string so we an directly compare
        return char == aStr # returns true of false
    else:
        if char == aStr[stringlength//2]: # check if character is the same as the char at the center of the string
            return True
        elif char < aStr[stringlength//2]: # check if character is 'lower than' the character halfway up the stringlength (alphabet is ranked)
            return isIn(char, aStr[:stringlength//2]) # recursion, rerun check with half the string length
                        
        else:
            return isIn(char, aStr[(stringlength//2)+1:])

print(isIn('e', 'abcdefghijklmnop'))
