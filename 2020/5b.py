#!/usr/bin/env python3

import fileinput

trans = str.maketrans('BFRL', '1010')
seat = lambda s: int(s.translate(trans), 2)
passes = {seat(line) for line in fileinput.input()}
seats = set(range(min(passes), max(passes)+1))
mine, = seats - passes
print(mine)
