#!/usr/bin/env python3

import fileinput
from intcode import Interpreter
import operator
from collections import defaultdict, deque
from more_itertools import last
import copy 

program = next(fileinput.input())

def display(pos, grid):
  out = []
  minx, miny = map(min, zip(*grid.keys()))
  maxx, maxy = map(max, zip(*grid.keys()))
  for y in range(miny, maxy+1):
    out.append(''.join(grid[x,y] if (x,y) != pos else 'D' for x in range(minx, maxx+1)))
  return '\n'.join(out)

def getinput():
  while True:
    d = input('dir [nsew]: ')
    m = {'n': 1, 's': 2, 'w': 3, 'e': 4}
    if d in m:
      return m[d]
    print("nope.", d, 'is not a valid instruction. try again')

def follow(path):
  m = Interpreter(program)
  m.input.extend(path)
  return last(m)

moves = [None, (0,-1), (0, 1), (-1, 0), (1, 0)]
grid = defaultdict(lambda: ' ', {(0,0): '.'})

def bfs(startpos, startm, target):
  curgen = ((startpos, startm),)
  visited = set([(0, 0)])
  pathlen = 0
  while curgen:
    nextgen = []
    for cur in curgen:
      pos, m = cur
      for i in range(1, 5):
        newpos = tuple(map(operator.add, pos, moves[i]))
        if newpos in visited:
          continue
        visited.add(newpos)
        newm = copy.deepcopy(m)
        value = newm.run(input=i, output=True)
        grid[newpos] = '#.O'[value]
        if value == target:
          return newpos, newm
        if value == 0:
          continue
        nextgen.append((newpos, newm))
    curgen = nextgen
    pathlen += 1
  return pathlen-1

opos, om = bfs((0,0), Interpreter(program), 2)
minutes = bfs(opos, om, None)
print(display(None, grid))
print(minutes)

# pos = (0,0)
# moves = [(0,-1), (0, 1), (-1, 0), (1, 0)]
# grid = defaultdict(lambda: ' ', {pos: '.'})
# while True:
#   instruction = int(getinput())
#   move = moves[instruction-1]
#   newpos = tuple(map(operator.add, pos, move))
#   sense = m.run(input=instruction, output=True)
#   grid[newpos] = '#.O'[sense]
#   pos = pos if sense == 0 else newpos
#   if sense == 2:
#     break
#   print(display(pos, grid))
#
# print(display((0,0), grid))