#!/usr/bin/env python3

import sys
import re

input = open(sys.argv[1]) if len(sys.argv) == 2 else sys.stdin

rules = dict(line.split(' bags contain ') for line in input.read().splitlines())

contents = lambda bag: sum(int(n) * (1 + contents(b)) for n, b in re.findall(r'(\d+) ([^,]+) bags?[,.]', rules[bag]))

print(contents('shiny gold'))
