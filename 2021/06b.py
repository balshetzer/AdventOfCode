#!/usr/bin/env python3

import fileinput
from collections import Counter

nums = list(map(int, next(fileinput.input()).strip().split(',')))
fish = Counter(nums)

for i in range(256):
  fish = Counter({k-1:v for k,v in fish.items()})
  if (spawn := fish[-1]) != 0:
    fish[8], fish[6] = spawn, fish[6] + spawn
    del fish[-1]
print(fish.total())
