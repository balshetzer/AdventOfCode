#!/usr/bin/env python3

import fileinput
import heapq
from collections import defaultdict
import math

def run():
  add = lambda a, b: (a[0] + b[0], a[1] + b[1])
  grid = {(x,y): int(d) for y, line in enumerate(fileinput.input()) for x, d in enumerate(line.strip())}
  width, height = add(max(grid), (1,1))
  risk = lambda x, y: (grid[x % width, y % height] + x // width + y // height - 1) % 9 + 1
  inside = lambda p: 0 <= p[0] < 5*width and 0 <= p[1] < 5*height
  start = (0,0) # top left
  end = (5*width-1, 5*height-1) # bottom right
  dirs = ((-1, 0), (0, -1), (1, 0), (0, 1)) # 4-way connected
  # manhattan distance as heuristic
  heuristic = lambda p: end[0] - p[0] + end[1] - p[1]

  costs = defaultdict(lambda: math.inf, {start: 0}) # lowest cost known to get to each node
  neighbors = lambda p: filter(inside, (add(p, d) for d in dirs))
  q = [(heuristic(start), start)] # cost + heuristic, node
  while q:
    cost, node = heapq.heappop(q)
    if node == end:
      print(cost)
      return
    cost -= heuristic(node)
    for neighbor in neighbors(node):
      neighbor_score = cost + risk(*neighbor)
      if neighbor_score < costs[neighbor]:
        heapq.heappush(q, (neighbor_score + heuristic(neighbor), neighbor))
        costs[neighbor] = neighbor_score

run()
