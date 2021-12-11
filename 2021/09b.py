#!/usr/bin/env python3

import fileinput
from itertools import product
from functools import reduce
from collections import Counter
from operator import mul

grid = {(width:=x,height:=y): int(digit) for y, line in enumerate(fileinput.input()) for x, digit in enumerate(line.strip()) if digit != '9'}
width, height = width+1, height+1

colors = {}
for p in filter(lambda p: p in grid, product(range(width), range(height))):
  x, y = p
  match (grid.get((x, y-1)),grid.get((x-1, y))):
    case (None, None):
      color = object()
      colors[color] = color
      grid[p] = color
    case (color, None)|(None, color):
      grid[p] = color
    case (up, left):
      colors[left] = up
      grid[p] = up

for color in colors:
  original = color
  while (newcolor := colors[color]) != color:
    color = newcolor
  if original != color:
    colors[original] = color 

top = Counter(colors[color] for color in grid.values()).most_common(3)
print(reduce(mul, (count for color, count in top)))
