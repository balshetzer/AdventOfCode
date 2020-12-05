#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

def valid(p):
  return len(p) - ('cid' in p) == 7

print(sum(valid(dict(field.split(':') for field in block.split())) for block in input.read().split('\n\n')))
