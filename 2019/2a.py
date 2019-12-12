#!/usr/bin/env python3

import fileinput
import intcode

program = list(map(int, next(fileinput.input()).strip().split(',')))
program[1] = 12
program[2] = 2
m = intcode.Interpreter(program)
m.run()
print(m.mem[0])
