#!/usr/bin/env python3

import fileinput

def valid(s):
  a, b, c = s.strip().split()
  x, y = [int(x) - 1 for x in a.split('-')]
  b = b[0]
  return (c[x] == b) != (c[y] == b)

print(sum(valid(line) for line in fileinput.input()))
