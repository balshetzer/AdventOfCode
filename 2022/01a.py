#!/usr/bin/env python3

import fileinput
from itertools import groupby

lines = (line.strip() for line in fileinput.input())
groups = (nums for isnum, nums in groupby(lines, lambda line: len(line) > 0) if isnum)
calories = (sum(int(num) for num in nums) for nums in groups)
print(max(calories))
