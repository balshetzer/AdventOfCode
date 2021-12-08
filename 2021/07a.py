#!/usr/bin/env python3

import fileinput
from collections import Counter

nums = list(map(int, next(fileinput.input()).strip().split(',')))
crabs = Counter(nums)

cost = lambda dest: sum(abs(dest-loc)*count for loc, count in crabs.items())
print(min(cost(candidate) for candidate in crabs.keys()))
