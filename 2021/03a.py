#!/usr/bin/env python3

import fileinput
from statistics import mode

data = [line.strip() for line in fileinput.input()]
columns = zip(*data)
modes = map(mode, columns)
gamma = int(''.join(modes), base=2)
epsilon = (1 << len(data[0])) - 1 - gamma # ~gamma
print(gamma * epsilon)
