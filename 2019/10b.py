#!/usr/bin/env python3

import fileinput
import math
from itertools import groupby
from more_itertools import roundrobin

def num_visible(p, asteroids):
  visible = set()
  for asteroid in asteroids:
    if p == asteroid:
      continue
    v = (asteroid[0]-p[0], asteroid[1]-p[1])
    d = math.gcd(*v)
    v = (v[0]/d, v[1]/d)
    visible.add(v)
  return len(visible)

def angle(base, p):
  '''Gives the clockwise angle to the up direction from base for p. 
  
  i.e. if you take a vector from base up and from base to p this is
  the angle you would rotate the vector to p counter-clockwise to 
  reach the up vector.'''
  return (math.atan2(p[1]-base[1], p[0]-base[0]) + math.pi/2 + 2 * math.pi) % (2 * math.pi)

def ordered(base, asteroids):
  angletobase = lambda x: angle(base, x)
  disttobase = lambda x: math.dist(base, x)
  asteroids = sorted(asteroids, key=angletobase)
  angle_groups = [sorted(group, key=disttobase) for _, group in groupby(asteroids, key=angletobase)]
  return list(roundrobin(*angle_groups))

asteroids = [(x, y) for y, line in enumerate(fileinput.input()) for x, cell in enumerate(line.strip()) if cell == '#']
base = max(asteroids, key=lambda p: num_visible(p, asteroids))
order = ordered(base, asteroids)
winner = order[199]
print(winner[0]*100 + winner[1])
