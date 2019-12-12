#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from intcode import Interpreter
import operator

program = next(fileinput.input())

machine = Interpreter(program)
position = (0,0)
dir = (0, -1)
surface = defaultdict(int, {position: 1})
while True:
  paint = machine.run(input=surface[position], output=True)
  if paint is None:
    break
  surface[position] = paint
  turn = machine.run(output=True)
  dir = (dir[1], -dir[0]) if turn == 0 else (-dir[1], dir[0])
  position = tuple(map(operator.add, dir, position))

exes, whys = map(list, zip(*surface.keys()))
for y in range(min(whys), max(whys) + 1):
  for x in range(min(exes), max(exes) + 1):
    print('#' if surface[(x, y)] == 1 else ' ', end='')
  print()
