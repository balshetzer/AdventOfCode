#!/usr/bin/env python3

import fileinput
from itertools import permutations
from intcode import Interpreter

program = next(fileinput.input())

def run(params):
  signal = 0
  machines = [Interpreter(program, input=[p]) for p in params]
  while True:
    for m in machines:
      out = m.run(input=signal, output=True)
      if out is None:
        return signal
      signal = out

print(max(map(run, permutations((5, 6, 7, 8, 9)))))
