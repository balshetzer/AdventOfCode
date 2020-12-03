#!/usr/bin/env python3

import fileinput
from math import prod
from itertools import starmap

slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]

hill = [line.strip() for line in fileinput.input()]

def trees(dx, dy):
  x = 0
  y = 0
  trees = 0
  while True:
    x += dx
    y += dy
    if y >= len(hill):
      break
    line = hill[y]
    trees += line[x%len(line)] == '#'
  return trees

print(prod(starmap(trees, slopes)))
