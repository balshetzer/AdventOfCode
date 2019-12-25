#!/usr/bin/env python3

from intcode import Interpreter
import fileinput
from collections import defaultdict
from itertools import starmap
import operator

grid = defaultdict(int)
m = Interpreter(next(fileinput.input()))
x = 0
y = 0
for c in m:
  if c == 10:
    x = 0
    y += 1
    print()
    continue
  grid[(x, y)] = c
  x += 1
  print(chr(c), end='')

def isnode(p):
  return (grid[p] == 35 and 
          grid[(p[0]+1, p[1])] == 35 and 
          grid[(p[0]-1, p[1])] == 35 and 
          grid[(p[0], p[1]+1)] == 35 and 
          grid[(p[0], p[1]-1)] == 35)

nodes = [k for k, v in list(grid.items()) if isnode(k)]
print(sum(starmap(operator.mul, nodes)))
