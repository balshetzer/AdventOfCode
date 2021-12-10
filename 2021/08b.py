#!/usr/bin/env python3

import fileinput
from collections import Counter
from itertools import starmap

def mapping(words):
  counts = Counter(''.join(words))
  words = [frozenset(word) for word in words]
  digits = {} 
  segments = {}
  # b is the segment that shows up in six digits
  segments['b'] = next(k for k,v in counts.items() if v == 6)
  # e is the segment that shows up in four digits
  segments['e'] = next(k for k,v in counts.items() if v == 4)
  # f is the segment that shows up in nine digits
  segments['f'] = next(k for k,v in counts.items() if v == 9)
  # 1 is the two segment digit
  digits['1'] = next(word for word in words if len(word) == 2)
  # c is the segment in 1 that is not f
  segments['c'] = next(c for c in digits['1'] if c != segments['f'])
  # 7 is the three segment digit
  digits['7'] = next(word for word in words if len(word) == 3)
  # a is the segment in 7 that's not in 1 
  segments['a'] = next(c for c in digits['7'] if c not in digits['1'])
  # 4 is the four segment digit
  digits['4'] = next(word for word in words if len(word) == 4)
  # d is the segment in 4 we haven't decoded yet
  segments['d'] = next(c for c in digits['4'] if c not in segments.values())
  # 8 is the seven segment digit
  digits['8'] = next(word for word in words if len(word) == 7)
  # g is the only remaining segment. 8 is a good placeholder for "all segments".
  segments['g'] = next(c for c in digits['8'] if c not in segments.values())
    
  # 0 has six segments and not d
  digits['0'] = next(word for word in words if len(word) == 6 and segments['d'] not in word)
  # 2 has five segments and not f
  digits['2'] = next(word for word in words if len(word) == 5 and segments['f'] not in word)
  # 5 has five segments and not c
  digits['5'] = next(word for word in words if len(word) == 5 and segments['c'] not in word)
  # 3 has five segments and isn't in digits yet
  digits['3'] = next(word for word in words if len(word) == 5 and word not in digits.values())
  # 6 has six segments and not c
  digits['6'] = next(word for word in words if len(word) == 6 and segments['c'] not in word)
  # 9 is the last digit
  digits['9'] = next(word for word in words if word not in digits.values())
  return {v:k for k,v in digits.items()}  

def decode(data, display):
  table = mapping(data)
  return int(''.join(table[frozenset(digit)] for digit in display))

lines = ([p.split() for p in l.split('|')] for l in fileinput.input())
print(sum(decode(*line) for line in lines))    
