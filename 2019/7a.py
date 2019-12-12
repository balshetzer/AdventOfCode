#!/usr/bin/env python3

import fileinput
from itertools import permutations
from intcode import Interpreter

program = next(fileinput.input())

def run(params):
  signal = 0
  for p in params:
    signal = Interpreter(program, input=(p, signal)).run(output=True)
  return signal

print(max(map(run, permutations((0, 1, 2, 3, 4)))))
