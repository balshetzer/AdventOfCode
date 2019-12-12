#!/usr/bin/env python3

import fileinput
import math
from collections import defaultdict

asteroids = [(x, y) for y, line in enumerate(fileinput.input()) for x, cell in enumerate(line.strip()) if cell == '#']

def num_visible(p):
  visible = set()
  for asteroid in asteroids:
    if p == asteroid:
      continue
    v = (asteroid[0]-p[0], asteroid[1]-p[1])
    d = math.gcd(*v)
    v = (v[0]/d, v[1]/d)
    visible.add(v)
  return len(visible)

print(max(map(num_visible, asteroids)))
