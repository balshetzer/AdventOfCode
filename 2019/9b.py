#!/usr/bin/env python3

import fileinput
from intcode import Interpreter

print(Interpreter(next(fileinput.input())).run(input=2, output=True))
