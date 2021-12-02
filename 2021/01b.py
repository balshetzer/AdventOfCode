#!/usr/bin/env python3

import fileinput
from more_itertools import pairwise, triplewise

nums = [int(line.strip()) for line in fileinput.input()]

print(sum(1 if b > a else 0 for a, b in pairwise(map(sum, triplewise(nums)))))
