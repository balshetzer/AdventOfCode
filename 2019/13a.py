#!/usr/bin/env python3

from intcode import Interpreter
import fileinput
from more_itertools import chunked

screen = {}
for x, y, id in chunked(Interpreter(next(fileinput.input())), 3):
  screen[x,y] = id
print(list(screen.values()).count(2))