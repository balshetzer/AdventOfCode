#!/usr/bin/env python3

import sys
import re

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

wanted = {'shiny gold'}
containers = set()

while wanted:
  wanted = {key for key, value in rules.items() if any(re.search(r'\d ' + bag + ' bag', value) for bag in wanted)}
  containers |= wanted
  
print(len(containers))

