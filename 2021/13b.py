#!/usr/bin/env python3

import fileinput
import parse
from ascii_art import image_to_text
from itertools import takewhile
from operator import truth

def run():
  lines = (line.strip() for line in fileinput.input())

  parse_point = parse.compile('{:d},{:d}')
  grid = set(parse_point.parse(line) for line in takewhile(truth, lines))

  parse_fold = parse.compile('fold along {:w}={:d}')

  def folder(axis, coord):
    def fold(foo):
      if foo < coord:
        return foo
      return coord - (foo - coord)
    if axis == 'x':
      return lambda p: (fold(p[0]), p[1])
    return lambda p: (p[0], fold(p[1]))

  for line in lines:
    axis, coord = parse_fold.parse(line).fixed
    fold = folder(axis, coord)
    grid = {fold(p) for p in grid}

  width = max(x for x, y in grid) + 1
  height = max(y for x, y in grid) + 1

  image = '\n'.join(''.join('#' if (x,y) in grid else ' ' for x in range(width)) for y in range(height))
  print(image_to_text(image))

run()