#!/usr/bin/env python3

import fileinput

hill = [line.strip() for line in fileinput.input()]

def count(dx, dy):
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

print(count(1, 1) * count(3, 1) * count(5, 1) * count(7, 1) * count(1, 2))
