#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

grid = {}
for j, line in enumerate(input.read().splitlines()):
  for i, c in enumerate(line):
    grid[(i, j)] = c

def show(grid):
  keys = sorted(grid.keys(), key=lambda p: p[1] * len(grid) + p[0])
  row = 0
  l = []
  for p in keys:
    if p[1] != row:
      l.append('\n')
      row = p[1]
    l.append(grid[p])
  return ''.join(l)
  
def step(grid):
  def adj(p):
    out = []
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
          continue
        q = (p[0] + dx, p[1] + dy)
        if q in grid:
          out.append(grid[q])
    return out
  new = grid.copy()
  for k, v in grid.items():
    if v == 'L':
      if adj(k).count('#') == 0:
        new[k] = '#'
    elif v == '#':
      if adj(k).count('#') >= 4:
        new[k] = 'L'
  return new
  
while True:
  new = step(grid)
  if new == grid:
    break
  grid = new
  
print(list(grid.values()).count('#'))
