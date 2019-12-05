#!/usr/bin/env python3

import fileinput

def valid(s):
    s = str(s)
    repeat_length = 0
    has_double = False
    prev = s[0]
    for c in s[1:]:
        if c < prev:
            return False
        if c == prev:
            repeat_length += 1
        else:
            if repeat_length == 1:
                has_double = True
            repeat_length = 0
        prev = c
    return has_double or repeat_length == 1

def count(start, end):
    return sum(1 for i in filter(valid, range(start, end+1)))

for line in fileinput.input():
    print(count(*map(int, line.split('-'))))
    break
