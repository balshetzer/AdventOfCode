#!/usr/bin/env python3

import fileinput
import re

def valid(s):
  m = re.match(r'(\d+)-(\d+) (\w): (\w+)', s)
  min, max = map(int, m.group(1, 2))
  c = m.group(3)
  p = m.group(4)
  return min <= p.count(c) <= max

print(sum(valid(line) for line in fileinput.input()))
