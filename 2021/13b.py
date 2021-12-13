#!/usr/bin/env python3

import fileinput
from collections import defaultdict
import parse
from ascii_art import image_to_text

lines = (line.strip() for line in fileinput.input())

parse_point = parse.compile('{:d},{:d}')

grid = defaultdict(int)
for line in lines:
  if line == '':
    break
    
  grid[parse_point.parse(line).fixed] = 1

parse_fold = parse.compile('fold along {:w}={:d}')

for line in lines:
  folded = {}
  axis, coord = parse_fold.parse(line).fixed
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
  grid = folded

width = max(x for x, y in grid) + 1
height = max(y for x, y in grid) + 1

image = '\n'.join(''.join('#' if (x,y) in grid else ' ' for x in range(width)) for y in range(height))
print(image_to_text(image))