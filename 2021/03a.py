#!/usr/bin/env python3

import fileinput
from more_itertools import unzip

data = (line.strip() for line in fileinput.input())
columns = unzip(data)
sums = [sum(1 if d == "1" else -1 for d in column) for column in columns]
gamma = ''.join('1' if sum > 0 else '0' for sum in sums)
gamma = int(gamma, base=2)
epsilon = (1 << len(sums)) - 1 - gamma # ~gamma
print(gamma * epsilon)