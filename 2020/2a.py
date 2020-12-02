#!/usr/bin/env python3

import fileinput

def valid(s):
  a, b, c = s.strip().split()
  min, max = map(int, a.split('-'))
  b = b[0]
  count = c.count(b)
  return min <= count <= max

print(sum(valid(line) for line in fileinput.input()))
