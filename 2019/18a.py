#!/usr/bin/env python3

import fileinput
import string
from collections import defaultdict
import heapq
import operator

ascii_lowercase = set(string.ascii_lowercase)
ascii_uppercase = set(string.ascii_uppercase)

grid = {(x, y): c for y, line in enumerate(fileinput.input()) for x, c in enumerate(line.strip())}
all_keys = ''.join(sorted(set(v for v in grid.values() if v in ascii_lowercase)))
start = {v: k for k, v in grid.items() if v == '@'}['@']

dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def astar():
  q = [(0, '', start)]  # state is (steps, keys, pos)
  heapq.heapify(q)
  visited = set([start, '']) # (pos, keys)
  while q:
    steps, keys, pos = heapq.heappop(q)
    for dir in dirs:
      newpos = tuple(map(operator.add, pos, dir))
      if (newpos, keys) in visited:
        continue
      cell = grid[newpos]
      if cell == '#' or cell in ascii_uppercase and cell.lower() not in keys:
        continue
      if cell in ascii_lowercase and cell not in keys:
        newkeys = ''.join(sorted(keys + cell))
        if newkeys == all_keys:
          return steps+1
        visited.add((newpos, keys))
      else:
        newkeys = keys
      visited.add((newpos, newkeys))
      heapq.heappush(q, (steps+1, newkeys, newpos))

print(astar())
