#!/usr/bin/env python3

import fileinput
import itertools

orbiter_to_orbitee = {}
for line in fileinput.input():
    a, b = line.strip().split(')')
    orbiter_to_orbitee[b] = a
    
def path_to_root(x):
    path = []
    while x in orbiter_to_orbitee:
        x = orbiter_to_orbitee[x]
        path.append(x)
    return path

def index_of_first_different(a, b):
    return next(i for i, (a, b) in enumerate(zip(a,b)) if a != b)

you = path_to_root('YOU')
san = path_to_root('SAN')
i = index_of_first_different(reversed(you), reversed(san))
print(len(you) + len(san) - 2 * i)
