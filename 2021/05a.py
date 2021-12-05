#!/usr/bin/env python3

import fileinput
import parse
from collections import defaultdict
from itertools import chain, repeat
from math import copysign

#from itertools import groupby, product
#from operator import truth

p = parse.compile('{:d},{:d} -> {:d},{:d}')
lines = (p.parse(line.strip()).fixed for line in fileinput.input())
lines = filter(lambda q: q[0] == q[2] or q[1] == q[3],lines)

def move(a, b, n):
  'Get an iterator that advances a to b n times, repeating b as needed.'
  return chain(range(a, b, int(copysign(1, b-a))), repeat(b, n - abs(b-a) + 1))

def walk(x1, y1, x2, y2):
  n = max(abs(x1-x2), abs(y1-y2))
  xs = move(x1, x2, n)
  ys = move(y1, y2, n)
  return zip(xs, ys)

points = (point for line in lines for point in walk(*line))

grid = defaultdict(int)
for point in points:
  grid[point] += 1

print(sum(1 for v in grid.values() if v > 1))
