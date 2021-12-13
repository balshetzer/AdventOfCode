#!/usr/bin/env python3

import fileinput
from collections import defaultdict

graph = defaultdict(list)
for left, right in (line.strip().split('-') for line in fileinput.input()):
  graph[left].append(right)
  graph[right].append(left)
  
paths = [('start', set(), False)]

finished = 0

def expand(path):
  global finished, paths
  tip, visited, doubled = path
  for n in graph[tip]:
    if n == 'start':
      pass
    elif n == 'end':
      finished += 1
    elif n.isupper():
      paths.append((n, visited, doubled))
    elif not n in visited:
      paths.append((n, visited | {n}, doubled))
    elif not doubled:
      paths.append((n, visited, True))

while paths:
  expand(paths.pop())

print(finished)
