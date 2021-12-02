#!/usr/bin/env python3

import fileinput
import parse

p = parse.compile("{:w} {:d}")

depth = 0
distance = 0
aim = 0
commands = (p.parse(line.strip()).fixed for line in fileinput.input())
for command in commands:
  match command:
    case ("forward", x):
      distance += x
      depth += aim * x
    case ("down", x):
      aim += x
    case ("up", x):
      aim -= x

print(depth * distance)
