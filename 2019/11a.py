#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from intcode import Interpreter
import itertools
import operator

program = next(fileinput.input())

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

machine = Interpreter(program)
position = (0,0)
dir = (0, -1)
surface = defaultdict(int)
while True:
  paint = machine.run(input=surface[position], output=True)
  if paint is None:
    break
  surface[position] = paint
  turn = machine.run(output=True)
  dir = (dir[1], -dir[0]) if turn == 0 else (-dir[1], dir[0])
  position = tuple(map(operator.add, dir, position))

print(len(surface))