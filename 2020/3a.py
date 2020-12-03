#!/usr/bin/env python3

import fileinput

hill = [line.strip() for line in fileinput.input()]

x = 0
trees = 0
for line in hill[1:]:
  x += 3
  trees += line[x%len(line)] == '#'
print(trees)