#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from intcode import Interpreter
import itertools
import operator

program = next(fileinput.input())

machine = Interpreter(program)
position = (0,0)
dir = (0, -1)
surface = defaultdict(int)
surface[position] = 1
while True:
  paint = machine.run(input=surface[position], output=True)
  if paint is None:
    break
  surface[position] = paint
  turn = machine.run(output=True)
  dir = (dir[1], -dir[0]) if turn == 0 else (-dir[1], dir[0])
  position = tuple(map(operator.add, dir, position))

exes, whys = map(list, zip(*surface.keys()))

minx = min(exes)
maxx = max(exes)
miny = min(whys)
maxy = max(whys)
for y in range(miny, maxy + 1):
  for x in range(minx, maxx + 1):
    print('#' if surface[(x, y)] == 1 else ' ', end='')
  print()
