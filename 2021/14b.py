#!/usr/bin/env python3

import fileinput
from itertools import pairwise
from collections import Counter

lines = (line.strip() for line in fileinput.input())

template = next(lines)
next(lines)

rules = {}
for line in lines:
  left, right = line.split(' -> ')
  first, second = left
  rules[left] = [first+right, right+second]

pairs = Counter(a+b for a, b in pairwise(template))

def insert(pairs, rules):
  new = Counter()
  for pair, count in pairs.items():
    for update in rules.get(pair, (pair,)):
      new.update({update: count})
  return new

def count(pairs):
  polymer = Counter((template[0], template[-1]))
  for (a, b), count in pairs.items():
    polymer.update({a: count})
    polymer.update({b: count})
  for key, value in polymer.items():
    polymer[key] = value // 2
  return polymer

for step in range(40):
  pairs = insert(pairs, rules)

polymer = count(pairs)

print(max(polymer.values()) - min(polymer.values()))
