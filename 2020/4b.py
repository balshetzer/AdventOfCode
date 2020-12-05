#!/usr/bin/env python3

import fileinput
import re

validators = {
  'byr': lambda v: 1920 <= int(v) <= 2002,
  'iyr': lambda v: 2010 <= int(v) <= 2020,
  'eyr': lambda v: 2020 <= int(v) <= 2030,
  'hgt': lambda v: re.fullmatch(r'\d+(in|cm)', v) and (59 <= int(v[:-2]) <= 76 if v[-2:] == 'in' else 150 <= int(v[:-2]) <= 193),
  'hcl': lambda v: re.fullmatch(r'#[0-9a-f]{6}', v),
  'ecl': lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
  'pid': lambda v: re.fullmatch(r'\d{9}', v),
}

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
    key, value = field.split(':')
    if key != 'cid' and validators[key](value):
      current += 1
else:
  if current == 7:
    valid += 1
    
print(valid)