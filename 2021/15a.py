#!/usr/bin/env python3

import fileinput
import heapq

def run():
  grid = {(x,y): int(d) for y, line in enumerate(fileinput.input()) for x, d in enumerate(line.strip())}
  start = (0,0) # top left
  end = max(grid) # bottom right
  dirs = ((-1, 0), (0, -1), (1, 0), (0, 1)) # 4-way connected
  # manhattan distance as heuristic
  heuristic = lambda p: end[0] - p[0] + end[1] - p[1]
  add = lambda a, b: (a[0] + b[0], a[1] + b[1])
  costs = {start: 0} # lowest cost known to get to each node
  neighbors = lambda p: filter(lambda x: x in grid and x, (add(p, d) for d in dirs))
  q = [(heuristic(start), start)] # cost + heuristic, node
  while q:
    cost, node = heapq.heappop(q)
    if node == end:
      print(cost)
      return
    cost -= heuristic(node)
    for neighbor in neighbors(node):
      neighbor_score = cost + grid[neighbor]
      if neighbor not in costs or neighbor_score < costs[neighbor]:
        heapq.heappush(q, (cost + grid[neighbor] + heuristic(neighbor), neighbor))
        costs[neighbor] = neighbor_score

run()
