#!/usr/bin/env python3

import fileinput

nums = set(int(line.strip()) for line in fileinput.input())

def f(sum):
  for num in nums:
    other = sum - num
    if other in nums:
      return num, other

for num in nums:
  others = f(2020-num)
  if others:
    print(num * others[0] * others[1])
    break
