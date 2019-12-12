#!/usr/bin/env python3

import fileinput
import math
from itertools import groupby
from more_itertools import roundrobin, nth

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

base = max(asteroids, key=num_visible)

def angle(p):
  '''Gives the clockwise angle to the up direction from base for p. 
  
  i.e. if you take a vector from base up and from base to p this is
  the angle you would rotate the vector to p counter-clockwise to 
  reach the up vector.'''
  return (math.atan2(p[1]-base[1], p[0]-base[0]) + math.pi/2 + 2 * math.pi) % (2 * math.pi)

dist = lambda x: math.dist(base, x)
asteroids.sort(key=angle)
angle_groups = [sorted(group, key=dist) for _, group in groupby(asteroids, key=angle)]
winner = nth(roundrobin(*angle_groups), 199)
print(winner[0]*100 + winner[1])
