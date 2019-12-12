#!/usr/bin/env python3

import fileinput
import intcode

m = intcode.Interpreter(next(fileinput.input()), input=[1])
while not m.halted():
  print(m.run(output=True))
