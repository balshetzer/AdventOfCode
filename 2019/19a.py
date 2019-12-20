#!/usr/bin/env python3

import fileinput
from intcode import Interpreter

program = next(fileinput.input())

grid = {}

def display(grid):
  out = []
  minx, miny = map(min, zip(*grid.keys()))
  maxx, maxy = map(max, zip(*grid.keys()))
  for y in range(miny, maxy+1):
    out.append(''.join(grid[x,y] for x in range(minx, maxx+1)))
  return '\n'.join(out)

sum = 0
for x in range(50):
  for y in range(50):
    v = Interpreter(program).run(input=[x, y], output=True)
    grid[x,y] = '#' if v else '.'
    sum += v

print(display(grid))

print(sum)
