#!/usr/bin/env python3

import fileinput

nums = [int(line.strip()) for line in fileinput.input()]

while nums:
  num = nums.pop()
  other = 2020-num
  if other in nums:
    print(num * other)
    break