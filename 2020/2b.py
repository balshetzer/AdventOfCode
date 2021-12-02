#!/usr/bin/env python3

import fileinput
import parse

parser = parse.compile("{:d}-{:d} {:w}: {:w}")

def valid(s):
  x, y, c, p = parser.parse(s).fixed
  return (p[x-1] == c) != (p[y-1] == c)

print(sum(valid(line.strip()) for line in fileinput.input()))
