#!/usr/bin/env python3

import fileinput

def add(pc, mem):
    mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
    return pc+4
    
def mul(pc, mem):
    mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
    return pc+4

def halt(pc, mem):
    return pc
    
opcodes = {1: add, 2: mul, 99: halt}

def interpret(pc, mem):
    return opcodes[mem[pc]](pc, mem)
    
def run(mem):
    pc = 0
    while True:
        oldpc, pc = pc, interpret(pc, mem)
        if oldpc == pc:
            return mem[0]

for line in fileinput.input():
    mem = list(map(int, line.strip().split(',')))
    mem[1] = 12
    mem[2] = 2
    print(run(mem))
    break
