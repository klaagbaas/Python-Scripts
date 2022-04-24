# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:12:54 2021

@author: Kaspar
"""

high = 100
low = 0
correct = 0

print("Please think of a number between 0 and 100!")
while correct == 0:
    guess = int((high+low)/2)
    print("Is your secret number", guess,"?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end = ' ')
    answer = input()
    if answer == "c":
        correct += 1
    elif answer == "l":
        low = guess
    elif answer == "h":
        high = guess
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", guess)
