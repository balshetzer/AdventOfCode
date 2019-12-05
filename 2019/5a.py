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
    mem[mem[pc+3]] = op(p1, p2)
    return pc+4

def add(pc, mem):
    return ternary_op(pc, mem, operator.add)
    
def mul(pc, mem):
    return ternary_op(pc, mem, operator.mul)

def halt(pc, mem):
    return pc
    
opcodes = {1: add, 2: mul, 3: input, 4: output, 99: halt}

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
