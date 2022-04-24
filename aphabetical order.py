# -*- coding: utf-8 -*-
s = "abbcxefgh"
length = 0
string = ""
for i in range(len(s)-1):
    j = i
    l = 1
    seq = s[j]
    while j < len(s)-1 and s[j] <= s[j+1]:
        seq += s[j+1]     
        j += 1
        l += 1
    if l > length:
        length = l
        string = seq
print("Longest substring in alphabetical order is:", string)
