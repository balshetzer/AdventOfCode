#!/usr/bin/env python3

import fileinput
from collections import defaultdict

def run():
  graph = defaultdict(list)
  for left, right in (line.strip().split('-') for line in fileinput.input()):
    graph[left].append(right)
    graph[right].append(left)
  
  paths = [('start', set(), False)]
  finished = 0

  while paths:
    path = paths.pop()
    tip, visited, doubled = path
    for n in graph[tip]:
      if n == 'start':
        pass
      elif n == 'end':
        finished += 1
      elif n[0].isupper():
        paths.append((n, visited, doubled))
      elif not n in visited:
        paths.append((n, visited | {n}, doubled))
      elif not doubled:
        paths.append((n, visited, True))
  print(finished)

run()
