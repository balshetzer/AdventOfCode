#!/usr/bin/env python3

import fileinput
import string
from collections import defaultdict
import heapq
import operator

ascii_lowercase = set(string.ascii_lowercase)
ascii_uppercase = set(string.ascii_uppercase)

def vadd(a, b):
  return (a[0] + b[0], a[1] + b[1])

dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

grid = {(x, y): c for y, line in enumerate(fileinput.input()) for x, c in enumerate(line.strip())}
all_keys = {v for v in grid.values() if v in ascii_lowercase}
start = {v: k for k, v in grid.items() if v == '@'}['@']
grid[start] = '#'
for dir in dirs:
  grid[vadd(start, dir)] = '#'
starts = (vadd(start, (-1, -1)), vadd(start, (-1, 1)), vadd(start, (1, -1)), vadd(start, (1, 1)))

def astar():
  q = [(0, frozenset(), starts)]  # state is (steps, keys, positions)
  heapq.heapify(q)
  visited = set([starts, frozenset()]) # (pos, keys)
  while q:
    steps, keys, poses = heapq.heappop(q)
    for i, pos in enumerate(poses):
      for dir in dirs:
        newpos = vadd(pos, dir)
        newposes = list(poses)
        newposes[i] = newpos
        newposes = tuple(newposes)
        if (newpos, keys) in visited:
          continue
        cell = grid[newpos]
        if cell == '#' or cell in ascii_uppercase and cell.lower() not in keys:
          continue
        if cell in ascii_lowercase and cell not in keys:
          newkeys = keys | frozenset([cell])
          if newkeys == all_keys:
            return steps+1
          visited.add((newpos, keys))
        else:
          newkeys = keys
        visited.add((newpos, newkeys))
        heapq.heappush(q, (steps+1, newkeys, newposes))

print(astar())
