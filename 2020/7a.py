#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

rules = defaultdict(set)
for line in input.read().splitlines():
  left = line.split(' bags', 1)[0]
  for bag in re.findall(r'\d+ ([^,]+) bags?[,.]', line):
    rules[bag].add(left)

bags = set()
q = {'shiny gold'}
while q:
  q = {b for x in q for b in rules[x]}
  bags |= q
print(len(bags))
