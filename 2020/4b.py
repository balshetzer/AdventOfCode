#!/usr/bin/env python3

import re
import sys

validators = {
  'byr': lambda v: 1920 <= int(v) <= 2002,
  'iyr': lambda v: 2010 <= int(v) <= 2020,
  'eyr': lambda v: 2020 <= int(v) <= 2030,
  'hgt': lambda v: re.fullmatch(r'\d+(in|cm)', v) and (59 <= int(v[:-2]) <= 76 if v[-2:] == 'in' else 150 <= int(v[:-2]) <= 193),
  'hcl': lambda v: re.fullmatch(r'#[0-9a-f]{6}', v),
  'ecl': lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
  'pid': lambda v: re.fullmatch(r'\d{9}', v),
}

def valid(p):
  return all(v(p[k]) if k in p else False for k, v in validators.items())

print(sum(valid(dict(field.split(':') for field in block.split())) for block in open(sys.argv[1]).read().split('\n\n')))
