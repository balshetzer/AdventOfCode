#!/usr/bin/env python3

import fileinput

def valid(s):
    s = str(s)
    has_repeat = False
    prev = s[0]
    for c in s[1:]:
        if c < prev:
            return False
        if c == prev:
            has_repeat = True
        prev = c
    return has_repeat

def count(start, end):
    return sum(1 for i in filter(valid, range(start, end+1)))

for line in fileinput.input():
    print(count(*map(int, line.split('-'))))
    break
