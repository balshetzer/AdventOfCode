#!/usr/bin/env python3

from intcode import Interpreter
import fileinput
from collections import defaultdict
from itertools import starmap, count, combinations
import operator
from more_itertools import first, last, substrings_indexes

def vadd(a, b):
  return (a[0] + b[0], a[1] + b[1])

def rotate_right(v):
  return (-v[1], v[0])
  
def rotate_left(v):
  return (v[1], -v[0])

program = next(fileinput.input())

def get_grid(program):
  m = Interpreter(program)
  grid = defaultdict(int)
  x = 0
  y = 0
  for c in m:
    if c == 10:
      x = 0
      y += 1
      continue
    grid[(x, y)] = c
    x += 1
  return grid

grid = get_grid(program)
width = max(map(first, grid.keys()))+1
height = max(map(last, grid.keys()))+1

def get_instructions(grid):
  start_pos = first(k for k,v in grid.items() if chr(v) in '<>^v')
  start_dir = (0, -1)

  cur_pos = start_pos
  cur_dir = start_dir
  instructions = []

  while True:
    right = rotate_right(cur_dir)
    #print('right is', right, 'pos at right is', vadd(cur_pos, right), 'value at right is', grid[vadd(cur_pos, right)] )
    left = rotate_left(cur_dir)  
    if grid[vadd(cur_pos, right)] == 35:
      cur_dir = right
      instructions.append('R')
    elif grid[vadd(cur_pos, left)] == 35:
      cur_dir = left
      instructions.append('L')
    else:
      return instructions
    for steps in count():
      next_pos = vadd(cur_pos, cur_dir)
      if grid[next_pos] == 35:
        cur_pos = next_pos
      else:
        instructions.append(str(steps))
        break

instructions = get_instructions(grid)

def run_robot(program, main, A, B, C, video=False):
  m = Interpreter(program)
  m.mem[0] = 2
  input = main + '\n' + A + '\n' + B + '\n' + C + '\n' + ('y' if video else 'n') + '\n'
  print(input)
  m.input.extend(map(ord, input))
  for c in m:
    if c <= 128:
      print(chr(c), end='')
    else:
      print(c)

def make_programs(instructions):
  groups = defaultdict(set)
  for seq, start, end in substrings_indexes(instructions):
    if len(seq) == 1:
      continue
    textprog = ','.join(seq)
    if len(textprog) > 20:
      continue
    groups[tuple(seq)].add(start)

  def startswith(l, sub):
    return len(sub) <= len(l) and all(map(operator.eq, l, sub))
  def make_main(instructions, subs):
    main = []
    # backtracking seems unnecessary
    while instructions:
      for i, sub in enumerate(subs):
        if startswith(instructions, sub):
          main.append('ABC'[i])
          instructions = instructions[len(sub):]
          if len(','.join(main)) > 20:
            return None
          break
      else:
        return None
    return main

  # start with longest subsequences
  subs = sorted(groups.keys(), key=len, reverse=True)
  for subs in combinations(subs, 3):
    main = make_main(instructions, subs)
    if main:
      return main, *subs

def verify_prog(instructions, main, A, B, C):
  main = main.split(',')
  subs = {'A': A, 'B': B, 'C': C}
  prog = []
  for i in main:
    prog.append(subs[i])
  prog = ','.join(prog)
  instructions = ','.join(instructions)
  return prog == instructions

subs = [','.join(sub) for sub in make_programs(instructions)]
#print(verify_prog(instructions, *subs))

print(run_robot(program, *subs))
