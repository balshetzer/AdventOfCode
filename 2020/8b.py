#!/usr/bin/env python3

import sys

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

parse = lambda data: [(a, int(b)) for a, b in (line.split() for line in data.splitlines())]

class Interpreter(object):
  def __init__(self, program):
    self.program = program
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
    
  def halts(self):
    seen = set([0])
    while self.pc < len(program):
      self.step()
      if self.pc in seen:
        return False
      seen.add(self.pc)
    return True

program = parse(input.read())

for i in range(len(program)):
  op = program[i]
  if op[0] not in {'nop', 'jmp'}:
    continue
  program[i] = ('jmp' if op[0] == 'nop' else 'nop', op[1])
  runner = Interpreter(program)
  if runner.halts():
    print(runner.accumulator)
    break
  program[i] = op
