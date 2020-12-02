#!/usr/bin/env python3

import fileinput

nums = set(int(line.strip()) for line in fileinput.input())

for num in nums:
  other = 2020-num
  if other in nums:
    print(num * other)
    break