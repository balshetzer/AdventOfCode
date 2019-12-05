#!/usr/bin/env python3

import fileinput
import operator

lines = fileinput.input()

def param(pc, mem, index):
    mode = mem[pc]//(10*10**index)%10
    if mode == 0:
        return mem[mem[pc+index]]
    else:
        return mem[pc+index]

def input(pc, mem):
    mem[mem[pc+1]] = int(next(lines).strip())
    return pc+2

def output(pc, mem):
    p1 = param(pc, mem, 1)
    print(p1)
    return pc+2

def ternary_op(pc, mem, op):
    p1 = param(pc, mem, 1)
    p2 = param(pc, mem, 2)
    mem[mem[pc+3]] = int(op(p1, p2))
    return pc+4

def add(pc, mem):
    return ternary_op(pc, mem, operator.add)
    
def mul(pc, mem):
    return ternary_op(pc, mem, operator.mul)

def jump_if_true(pc, mem):
    p1 = param(pc, mem, 1)
    p2 = param(pc, mem, 2)
    return p2 if p1 != 0 else pc+3

def jump_if_false(pc, mem):
    p1 = param(pc, mem, 1)
    p2 = param(pc, mem, 2)
    return p2 if p1 == 0 else pc+3

def less_than(pc, mem):
    return ternary_op(pc, mem, operator.lt)
    
def equals(pc, mem):
    return ternary_op(pc, mem, operator.eq)

def halt(pc, mem):
    return pc
    
opcodes = {1: add, 2: mul, 3: input, 4: output, 5: jump_if_true, 
           6: jump_if_false, 7: less_than, 8: equals, 99: halt}

def interpret(pc, mem):
    return opcodes[mem[pc]%100](pc, mem)
    
def run(mem):
    pc = 0
    while True:
        oldpc, pc = pc, interpret(pc, mem)
        if oldpc == pc:
            break


mem = list(map(int, next(lines).strip().split(',')))
run(mem)
