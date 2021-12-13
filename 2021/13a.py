#!/usr/bin/env python3

import fileinput
from collections import defaultdict
import parse

lines = (line.strip() for line in fileinput.input())

parse_point = parse.compile('{:d},{:d}')

grid = defaultdict(int)
for line in lines:
  if line == '':
    break
    
  grid[parse_point.parse(line).fixed] = 1

parse_fold = parse.compile('fold along {:w}={:d}')

axis, coord = parse_fold.parse(next(lines)).fixed

folded = {}

match axis:
  case 'y':
    for x, y in grid:
      if y > coord:
        y = coord - (y - coord)
      folded[x,y] = 1
  case 'x':
    for x, y in grid:
      if x > coord:
        x = coord - (x - coord)
      folded[x,y] = 1

print(len(folded))