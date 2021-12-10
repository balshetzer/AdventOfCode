#!/usr/bin/env python3

import fileinput

lines = (map(len, line.split('|')[1].split()) for line in fileinput.input())
print(sum(sum(1 for n in line if n in {2, 4, 3, 7}) for line in lines))
