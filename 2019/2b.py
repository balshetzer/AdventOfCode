#!/usr/bin/env python3

import fileinput
import intcode

program = list(map(int, next(fileinput.input()).strip().split(',')))

def run(noun, verb):
  program[1] = noun
  program[2] = verb
  m = intcode.Interpreter(program)
  m.run()
  return m.mem[0]

def search():
  for noun in range(100):
    for verb in range(100):
      if run(noun, verb) == 19690720:
        return 100 * noun + verb

print(search())
