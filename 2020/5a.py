#!/usr/bin/env python3

import fileinput

def seat(s):
  rowend = 128
  rowbegin = 0
  colend = 8
  colbegin = 0
  for c in s:
    if c == "F":
      rowend -= (rowend-rowbegin)//2
    elif c == "B":
      rowbegin += (rowend-rowbegin)//2
    elif c == "L":
      colend -= (colend-colbegin)//2
    elif c == "R":
      colbegin += (colend-colbegin)//2
  return 8 * rowbegin + colbegin

print(max(seat(line) for line in fileinput.input()))
