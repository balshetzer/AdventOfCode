#!/usr/bin/env python3

import fileinput
from itertools import permutations
import operator
import math
from sys import stderr

def cmp(a, b):
    return (a > b) - (a < b)

class Moon:
  def __init__(self, input):
    self.pos = list(int(x.split('=')[1].strip()) for x in input.strip('<>').split(','))
    self.vel = [0, 0, 0]

  def pull(self, pullee):
    pullee.vel = list(map(operator.add, pullee.vel, map(cmp, self.pos, pullee.pos)))

  def translate(self):
    self.pos = list(map(operator.add, self.pos, self.vel))

  def energy(self):
    return sum(map(abs, self.pos)) * sum(map(abs, self.vel))

  def __str__(self):
    return 'pos=<x={}, y={}, z={}>, vel=<x={}, y={},z={}>'.format(*self.pos, *self.vel)

lines = fileinput.input()
iterations = int(next(lines))
moons = [Moon(line.strip()) for line in lines]

print('After 0 steps:', file=stderr)
for moon in moons:
  print(moon, file=stderr)

pairings = tuple(permutations(moons, 2))
for step in range(iterations):
  print('After', step+1, 'steps:', file=stderr)
  for puller, pullee in pairings:
    puller.pull(pullee)
  for moon in moons:
    moon.translate()
    print(moon, file=stderr)

print(sum(map(Moon.energy, moons)))
