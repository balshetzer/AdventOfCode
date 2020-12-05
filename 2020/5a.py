#!/usr/bin/env python3

import fileinput

trans = str.maketrans('BFRL', '1010')
seat = lambda s: int(s.translate(trans), 2)
print(max(seat(line) for line in fileinput.input()))
