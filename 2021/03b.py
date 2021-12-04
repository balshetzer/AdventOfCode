#!/usr/bin/env python3

import fileinput
import statistics

data = [line.strip() for line in fileinput.input()]

def mode(l):
  modes = statistics.multimode(l)
  return modes[0] if len(modes) == 1 else "1"

def antimode(l):
  return "1" if mode(l) == "0" else "0"

def metric(data, select):
  for i in range(len(data[0])):
    column = (n[i] for n in data)
    d = select(column)
    data = [s for s in data if s[i] == d]
    if len(data) == 1:
      return int(data[0], base=2)

def O2(data):
  return metric(data, mode)

def CO2(data):
  return metric(data, antimode)

print(O2(data) * CO2(data))
