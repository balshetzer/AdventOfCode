#!/usr/bin/env python3

import fileinput
from itertools import groupby, product
from operator import truth
from more_itertools import last

lines = (line.strip() for line in fileinput.input())
nums = map(int, next(lines).split(','))
grids = (list(g) for k, g in groupby(lines, truth) if k)

class Card:
  def __init__(self, lines):
    self._rows = [list(map(int, line.split())) for line in lines]
    self._won = False

  def mark(self, num):
    '''Mark the number on the card if still playing. Return score if won, otherwise None.'''
    if self._won:
      return None
    for row in self._rows:
      for i, v in enumerate(row):
        if v == num:
          row[i] = None
          if not any(row) or not any(row[i] for row in self._rows):
            self._won = True
            return num * sum(sum(filter(truth, row)) for row in self._rows)

cards = [Card(grid) for grid in grids]
turns = (card.mark(num) for num, card in product(nums, cards))
winners = (x for x in turns if x is not None)
print(last(winners))
