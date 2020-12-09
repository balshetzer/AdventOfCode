#!/usr/bin/env python3

import sys
import re
from collections import namedtuple
import types

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

class Interpreter(object):
  def __init__(self, program):
    self.program = [(a, int(b)) for a, b in (line.split() for line in program.splitlines())]
    self.pc = 0
    self.accumulator = 0

  def step(self):
    op = self.program[self.pc]
    getattr(self, op[0])(op)
    
  def nop(self, op):
    self.pc += 1
    
  def acc(self, op):
    self.pc += 1
    self.accumulator += op[1]
    
  def jmp(self, op):
    self.pc += op[1]

runner = Interpreter(input.read())
seen = set([0])
while True:
  runner.step()
  if runner.pc in seen:
    print(runner.accumulator)
    break
  seen.add(runner.pc)
