#!/usr/bin/env python3

import fileinput
from collections import defaultdict

graph = defaultdict(list)
for left, right in (line.strip().split('-') for line in fileinput.input()):
  graph[left].append(right)
  graph[right].append(left)
paths = [('start', {'start'})]
def expand(path):
  tip, visited = path
  if tip == 'end':
    return [path]
  return [(n, visited | {n}) for n in graph[tip] if n.isupper() or n not in visited]
  
while True:
  newpaths = []
  for path in paths:
    newpaths.extend(expand(path))
  if paths == newpaths:
    break
  paths = newpaths

print(len(paths))
