#!/usr/bin/env python3

import fileinput
from intcode import Interpreter
from collections import defaultdict
import itertools

program = next(fileinput.input())

grid = defaultdict(int)

# def display(grid):
#   out = []
#   minx, miny = map(min, zip(*grid.keys()))
#   maxx, maxy = map(max, zip(*grid.keys()))
#   for y in range(miny, maxy+1):
#     out.append(''.join(grid[x,y] for x in range(minx, maxx+1)))
#   return '\n'.join(out)



def lookup(x, y):
  p = (x, y)
  if p in grid:
    return grid[p]
  if p[0] < 0 or p[1] < 0:
    return 0
  v = Interpreter(program).run(input=p, output=True)
  grid[p] = v
  return v

def find_start(x, y):
  for start in range(x, x+4):
    if lookup(start, y) == 1:
      return start
  return None

def find_end(x, y):
  if lookup(x,y) == 1:
    x+=1
    while lookup(x,y) == 1:
      x+=1
    return x
  for end in range(x, x-5, -1):
    if lookup(end, y) == 1:
      return end
  return None

def down(x, y):
  len = 0
  while lookup(x, y) == 1:
    len += 1
    y += 1
  return len

def find():
  last_start = 0
  last_len = 0
  for y in itertools.count():
    x = last_start
    start = find_start(x, y)
    if not start:
      last_start += 1
      continue
    last_start = start
    end = find_end(start + last_len, y)
    if not end:
      print("what???", x, y)
    last_len = end - start
    for x in range(start, end):
      if end - x >= 100 and down(x, y) >= 100:
        return x * 10000 + y

print(find())