#!/usr/bin/env python3

import fileinput
import parse

parser = parse.compile("{:d}-{:d} {:w}: {:w}")

def valid(s):
  min, max, c, p = parser.parse(s).fixed
  return min <= p.count(c) <= max

print(sum(valid(line.strip()) for line in fileinput.input()))
