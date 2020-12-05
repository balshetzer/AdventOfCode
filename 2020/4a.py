#!/usr/bin/env python3

import fileinput

valid = 0
current = 0
for line in fileinput.input():
  line = line.strip()
  if len(line) == 0:
    if current == 7:
      valid += 1
    current = 0
    
  fields = line.split()
  for field in fields:
    key = field.split(':')[0]
    if key != 'cid':
      current += 1
else:
  if current == 7:
    valid += 1
    
print(valid)