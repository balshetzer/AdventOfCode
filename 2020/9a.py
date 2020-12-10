#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

data = [int(x) for x in input.read().splitlines()]

def valid(n, nums):
  for x in nums:
    y = n-x
    if y != x and y in nums:
      return True
  return False
  
N = 25

for i in range(N, len(data)):
  num = data[i]
  if not valid(num, set(data[i-N:i])):
    print(data[i])
    break