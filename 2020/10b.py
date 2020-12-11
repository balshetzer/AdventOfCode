#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

data = [0] + sorted([int(x) for x in input.read().splitlines()])

ways = [0] * len(data)
ways[0] = 1
for i in range(len(data)):
  w = ways[i]
  n = data[i]
  for j in [1, 2, 3]:
    j = i + j
    if j < len(data):
      if data[j] - n <= 3:
        ways[j] += w
print(ways[-1])
