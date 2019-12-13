#!/usr/bin/env python3

import fileinput
from itertools import count, permutations
from functools import reduce
from math import gcd

def lcm(nums):
  return reduce(lambda a, b: a * b // gcd(a, b), nums)

starts = tuple(tuple(int(coord.split('=')[1]) for coord in line.strip('\n<>').split(',')) for line in fileinput.input())
dimensions = len(starts[0])
periodicity = []
for dim in range(dimensions):
  moons = tuple([moon[dim], 0] for moon in starts)
  pairings = tuple(permutations(moons, 2))
  states = set()
  for step in count():
    state = tuple(map(tuple, moons))
    if state in states:
      periodicity.append(step)
      break
    states.add(state)
    for puller, pullee in pairings:
      pullee[1] += 0 if puller[0] == pullee[0] else 1 if puller[0] > pullee[0] else -1
    for moon in moons:
      moon[0] += moon[1]

print(lcm(periodicity))
