#!/usr/bin/env python3

import fileinput
import re

def valid(s):
  m = re.match(r'(\d+)-(\d+) (\w): (\w+)', s)
  x, y = (int(x) - 1 for x in m.group(1, 2))
  c = m.group(3)
  p = m.group(4)
  return (p[x] == c) != (p[y] == c)

print(sum(valid(line) for line in fileinput.input()))
