#!/usr/bin/env python3

import sys

def valid(p):
  return len(p) - ('cid' in p) == 7

print(sum(valid(dict(field.split(':') for field in block.split())) for block in open(sys.argv[1]).read().split('\n\n')))
