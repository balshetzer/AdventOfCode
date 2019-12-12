#!/usr/bin/env python3

import fileinput

def fuel(x):
  f = x//3-2
  return f + fuel(f) if f > 0 else 0

print(sum(fuel(int(line.strip())) for line in fileinput.input()))