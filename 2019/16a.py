#!/usr/bin/env python3

import fileinput
from itertools import repeat, cycle, islice
import operator

base_pattern = [0, 1, 0, -1]

def repeat_elements(it, i):
  for elem in it:
    yield from repeat(elem, i)

def pattern(index):
  gen = cycle(repeat_elements(base_pattern, index+1))
  next(gen)
  yield from gen

def next_digit(signal, index):
  return abs(sum(map(operator.mul, signal, pattern(index)))) % 10

def next_signal(signal):
  return [next_digit(signal, i) for i, _ in enumerate(signal)]

signal = [int(i) for i in next(fileinput.input()).strip()]
for i in range(100):
  signal = next_signal(signal)

print(''.join(map(str, signal[:8])))
