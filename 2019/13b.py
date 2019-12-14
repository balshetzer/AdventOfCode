#!/usr/bin/env python3

from intcode import Interpreter
import fileinput
from more_itertools import chunked
from time import sleep

def cmp(a, b):
    return (a > b) - (a < b)

objects = ' #%=o'

screen = {}
def draw():
  print("Score:", screen[-1, 0])
  max_x, max_y = map(max, zip(*screen.keys()))
  for y in range(max_y+1):
    for x in range(max_x+1):
      print(objects[screen[x,y]], end='')
    print()
  print()

m = Interpreter(next(fileinput.input()))
m.mem[0] = 2
ball_x = None
paddle_x = None
score = None
while not m.halted():
  for x, y, id in chunked(m, 3):
    screen[x,y] = id
    if id == 4:
      ball_x = x
    elif id == 3:
      paddle_x = x
    if (x, y) == (-1, 0):
      score = id
  draw()
  m.input.append(cmp(ball_x, paddle_x))
  sleep(.01)
print(score)
