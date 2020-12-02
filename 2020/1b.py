#!/usr/bin/env python3

import fileinput

nums = [int(line.strip()) for line in fileinput.input()]

def f(sum, nums):
  while nums:
    num = nums.pop()
    other = sum - num
    if other in nums:
      return num * other

while nums:
  num = nums.pop()
  others = f(2020-num, nums.copy())
  if others:
    print(num * others)
    break
