# -*- coding: utf-8 -*-
string = "abbcxefghwdvlksfjikjlmwfodkjdasg"
sublength = 0
substring = ""
for letter in range(len(string)-1):
    location = letter
    length = 1
    seq = string[location]
    while location < len(string)-1 and string[location] <= string[location+1]:
        seq += string[location+1]     
        location += 1
        length += 1
    if length > sublength:
        sublength = length
        substring = seq
print("Longest substring in alphabetical order is:", substring)
