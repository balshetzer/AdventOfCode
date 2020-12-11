#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

data = sorted([int(x) for x in input.read().splitlines()])
data = [0] + data + [data[-1]+3]
diffs = [j-i for i, j in zip(data[:-1], data[1:])]
print(diffs.count(1) * diffs.count(3))
