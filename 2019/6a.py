#!/usr/bin/env python3

import fileinput

orbits = {b: a for a, b in (line.strip().split(')') for line in fileinput.input())}
    
def parents(x):
    parents = 0
    while x in orbits:
        parents += 1
        x = orbits[x]
    return parents

print(sum(parents(k) for k in orbits.keys()))    