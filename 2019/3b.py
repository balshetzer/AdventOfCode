#!/usr/bin/env python3

import fileinput
import operator
import itertools

dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def wire(steps):
    add = lambda a,b: tuple(map(operator.add, a, b))
    result = [(0,0)]
    for step in steps.split(','):
        for dir in itertools.repeat(dirs[step[0]], int(step[1:])):
            result.append(add(result[-1], dir))
    return result

def crossing(a, b):
    dist = lambda p: a.index(p) + b.index(p)
    points = set(a[1:]).intersection(set(b[1:]))
    return min(map(dist, points))

wire1, wire2 = [wire(line.strip()) for line in itertools.islice(fileinput.input(), 2)]
print(crossing(wire1, wire2))
