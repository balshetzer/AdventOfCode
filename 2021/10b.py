#!/usr/bin/env python3

import fileinput
from itertools import pairwise
from statistics import median
from functools import reduce
from more_itertools import chunked

lines = (line.strip() for line in fileinput.input())
ends = {')': '(', ']': '[', '}': '{', '>': '<'}
bounty = {'(': 1, '[': 2, '{': 3, '<': 4}

def score(line):
  stack = []
  for c in line:
    if c in ends:
      opener = stack.pop()
      if ends[c] != opener:
        return None
    else:
      stack.append(c)
  return reduce(lambda score, opener: score*5 + bounty[opener], reversed(stack), 0)

print(median(filter(lambda x: x is not None, map(score, lines)))) 
