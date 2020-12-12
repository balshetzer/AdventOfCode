#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

dirs = [(1,0), (0,-1), (-1,0), (0,1)]

x, y = 0, 0
dx, dy = 1, 0

for line in input.read().splitlines():
  c, n = line[0], int(line[1:])
  if c == 'N':
    y += n
  elif c == 'S':
    y -= n
  elif c == 'E':
    x += n
  elif c == 'W':
    x -= n
  elif c == 'F':
    x += n*dx
    y += n*dy
  elif c == 'R':
    n %= 360
    if n == 90:
      dx, dy = dy, -dx
    elif n == 180:
      dx, dy = -dx, -dy
    elif n == 270:
      dx, dy = -dy, dx
  elif c == 'L':
    n %= 360
    if n == 90:
      dx, dy = -dy, dx
    elif n == 180:
      dx, dy = -dx, -dy
    elif n == 270:
      dx, dy = dy, -dx

print(abs(x) + abs(y))
