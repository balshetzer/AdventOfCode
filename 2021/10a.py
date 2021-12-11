#!/usr/bin/env python3

import fileinput

lines = (line.strip() for line in fileinput.input())
bounty = {')': 3, ']': 57, '}': 1197, '>': 25137}
ends = {')': '(', ']': '[', '}': '{', '>': '<'}

def score(line):
  stack = []
  for c in line:
    if c in ends:
      opener = stack.pop()
      if ends[c] != opener:
        return bounty[c]
    else:
      stack.append(c)
  return 0

print(sum(score(line) for line in lines))
