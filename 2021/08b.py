#!/usr/bin/env python3

import fileinput
from collections import Counter
from itertools import starmap

def mapping(words):
  counts = Counter(''.join(words))
  words = [frozenset(word) for word in words]
  digits = {} 
  # b is the segment that shows up in six digits
  b = next(k for k,v in counts.items() if v == 6)
  # f is the segment that shows up in nine digits
  f = next(k for k,v in counts.items() if v == 9)
  # 1 is the two segment digit
  digits['1'] = next(word for word in words if len(word) == 2)
  # c is the segment in 1 that is not f
  c = next(c for c in digits['1'] if c != f)
  # 7 is the three segment digit
  digits['7'] = next(word for word in words if len(word) == 3)
  # 4 is the four segment digit
  digits['4'] = next(word for word in words if len(word) == 4)
  # d is the segment in 4 that occurs seven times
  d = next(c for c in digits['4'] if counts[c] == 7)
  # 8 is the seven segment digit
  digits['8'] = next(word for word in words if len(word) == 7)
    
  # 0 has six segments and not d
  digits['0'] = next(word for word in words if len(word) == 6 and d not in word)
  # 2 has five segments and not f
  digits['2'] = next(word for word in words if len(word) == 5 and f not in word)
  # 5 has five segments and not c
  digits['5'] = next(word for word in words if len(word) == 5 and c not in word)
  # 3 has five segments and isn't in digits yet
  digits['3'] = next(word for word in words if len(word) == 5 and word not in digits.values())
  # 6 has six segments and not c
  digits['6'] = next(word for word in words if len(word) == 6 and c not in word)
  # 9 is the last digit
  digits['9'] = next(word for word in words if word not in digits.values())

  return {v:k for k,v in digits.items()}  

def decode(data, display):
  table = mapping(data)
  return int(''.join(table[frozenset(digit)] for digit in display))

lines = ([p.split() for p in l.split('|')] for l in fileinput.input())
print(sum(decode(*line) for line in lines))    
