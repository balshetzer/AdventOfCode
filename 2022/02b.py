#!/usr/bin/env python3

from sys import argv, stdin

f = open(argv[1]) if len(argv) == 2 else stdin


decode = {'A': {'X': 0+3 ,'Y': 3+1, 'Z': 6+2},
          'B': {'X': 0+1 ,'Y': 3+2, 'Z': 6+3},
          'C': {'X': 0+2 ,'Y': 3+3, 'Z': 6+1}}

score = lambda they, result: decode[they][result]

print(sum(score(*line.split(' ')) for line in f.read().strip().split('\n')))
