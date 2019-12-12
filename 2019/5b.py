#!/usr/bin/env python3

import fileinput
import intcode

print(intcode.Interpreter(next(fileinput.input())).run(input=5, output=True))
