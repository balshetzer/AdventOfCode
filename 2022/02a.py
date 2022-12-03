#!/usr/bin/env python3

from sys import argv, stdin

f = open(argv[1]) if len(argv) == 2 else stdin


decode = {'A': {'X': 3+1 ,'Y': 6+2, 'Z': 0+3},
          'B': {'X': 0+1 ,'Y': 3+2, 'Z': 6+3},
          'C': {'X': 6+1 ,'Y': 0+2, 'Z': 3+3}}

score = lambda they, result: decode[they][result]

print(sum(score(*line.split(' ')) for line in f.read().strip().split('\n')))
