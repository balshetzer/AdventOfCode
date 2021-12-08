#!/usr/bin/env python3

import fileinput
from collections import Counter

nums = list(map(int, next(fileinput.input()).strip().split(',')))
crabs = Counter(nums)

sum1ton = lambda n: n * (n+1) // 2
cost = lambda dest: sum(sum1ton(abs(dest-loc))*count for loc, count in crabs.items())
print(min(cost(candidate) for candidate in range(min(crabs.keys()), max(crabs.keys())+1)))

