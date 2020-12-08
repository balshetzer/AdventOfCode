#!/usr/bin/env python3

import sys
import re
import functools

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

# rules = {}
# for line in input.read().splitlines()):
#   left, right = line.split(' bags contain ')
#   if right == 'no other bags':
#     right = set()
#   else:
#     right = {x.split(' ', 1)[1] for x in right.split(', ')}
#   rules[left] = right

rules = dict(line.split(' bags contain ') for line in input.read().splitlines())

@functools.lru_cache(maxsize=None)
def contains(bag):
  v = rules[bag]
  if v == 'no other bags.':
    return 0
  total = 0
  for entry in v.split(', '):
    print(entry)
    n, rest = entry.split(' ', 1)
    n = int(n)
    bag, _ = rest.rsplit(' ', 1)
    total += n + n * contains(bag)
  return total

print(contains('shiny gold'))
