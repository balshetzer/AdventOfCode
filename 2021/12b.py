#!/usr/bin/env python3

import fileinput
from collections import defaultdict

graph = defaultdict(list)
for left, right in (line.strip().split('-') for line in fileinput.input()):
  graph[left].append(right)
  graph[right].append(left)
  
paths = [('start', {'start'}, False, ['start'])]

def expand(path):
  tip, visited, doubled, seq = path
  if tip == 'end':
    return [path]
  return [(n, visited | {n}, n.islower() and n in visited or doubled, seq + [n]) for n in graph[tip] if n.isupper() or n not in visited or n != 'start' and not doubled]

while True:
  newpaths = []
  for path in paths:
    newpaths.extend(expand(path))
  if paths == newpaths:
    break
  paths = newpaths

print(len(paths))

# grid = {(width:=x,height:=y): int(digit) for y, line in enumerate(fileinput.input()) for x, digit in enumerate(line.strip())}
# width, height = width+1, height+1
# dirs = tuple((dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if not dx == dy == 0)
# neighbors = lambda p: tuple(filter(lambda p: p in grid, ((p[0]+dx, p[1]+dy) for dx, dy in dirs)))
#
# def step():
#   # Step 1: Increment energy levels.
#   for point in grid:
#     grid[point] += 1
#
#   # Step 2: Flash
#   flashed = set()
#   def flash(p):
#     flashed.add(p)
#     for n in neighbors(p):
#       grid[n] += 1
#   def flashall():
#     did_flash = False
#     for point, value in grid.items():
#       if value > 9 and not point in flashed:
#         flash(point)
#         did_flash = True
#     return did_flash
#   while flashall(): pass
#
#   # Step 3: exhaust flashed
#   for p in flashed:
#     grid[p] = 0
#
#   return len(flashed)
#
# print(sum(step() for _ in range(100)))
#
# def printgrid():
#   for y in range(height):
#     print(''.join(str(grid[x,y]) for x in range(width)))
#   print()
