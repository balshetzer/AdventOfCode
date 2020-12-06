#!/usr/bin/env python3

import sys
input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

print(sum(len(set(b)) - ('\n' in b) for b in input.read().split('\n\n')))
