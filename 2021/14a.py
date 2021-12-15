#!/usr/bin/env python3

import fileinput
from itertools import pairwise
from collections import Counter

lines = (line.strip() for line in fileinput.input())

polymer = tuple((next(lines)))
next(lines)

rules = {}
for line in lines:
  left, right = line.split(' -> ')
  rules[tuple(left)] = right

for step in range(10):
  new = [polymer[0]]
  for first, second in pairwise(polymer):
    if (first,second) in rules:
      new.append(rules[(first,second)])
    new.append(second)
  polymer = new

c = Counter(polymer)
print(max(c.values()) - min(c.values()))