#!/usr/bin/env python3
for i in range(26):
    char = chr(ord('a') + i)
    if char != 'q' and char != 'e':
        print(char, end="")
