#!/usr/bin/env python3

import fileinput
from collections import Counter

nums = list(map(int, next(fileinput.input()).strip().split(',')))
fish = Counter(nums)

for i in range(256):
  fish = Counter({k-1:v for k,v in fish.items()})
  if -1 in fish:
    fish[8], fish[6] = fish[-1], fish[6] + fish[-1]
    del fish[-1]
print(fish.total())
