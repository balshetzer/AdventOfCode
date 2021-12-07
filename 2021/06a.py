#!/usr/bin/env python3

import fileinput

nums = list(map(int, next(fileinput.input()).strip().split(',')))
for i in range(80):
  nums = list(map(lambda x: x - 1, nums))
  births = sum(1 if x == -1 else 0 for x in nums)
  nums = list(map(lambda x: 6 if x == -1 else x, nums)) + [8]*births
print(len(nums))
