#!/usr/bin/env python3

import fileinput
import operator
import itertools

lines = fileinput.input()

def param(pc, mem, index):
    mode = mem[pc]//(10*10**index)%10
    if mode == 0:
        return mem[mem[pc+index]]
    else:
        return mem[pc+index]

global_inputs = []
global_outputs = []

def input(pc, mem):
    if len(global_inputs) == 0:
        print("inputs not available")
        return pc
    v = global_inputs.pop(0)
    print("read input", v)
    mem[mem[pc+1]] = v
    return pc+2

def output(pc, mem):
    p1 = param(pc, mem, 1)
    print("wrote output", p1)
    global_outputs.append(p1)
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
            if len(global_outputs) > 0:
                v = global_outputs.pop(0)
                print("yielding value", v)
                yield v
                continue
            if mem[pc] == 99:
                return
            yield None

program = list(map(int, next(lines).strip().split(',')))

def run_sequence(params):
    global global_inputs
    global global_outputs
    global_inputs = []
    machines = [run(program.copy()) for p in params]
    for m, p in zip(machines, params):
        global_inputs.append(p)
        if next(m) is not None:
            print("yikes")
    print("initialized")
    
    signal = 0
    try:
        while True:
            print("1 signal is", signal)
            for m in machines:
                global_inputs.append(signal)
                signal = next(m)
                print("2 signal is", signal)
                if signal is None:
                    print("oops")
    except:
        pass
    print("returning")
    return signal

print(max(map(run_sequence, itertools.permutations((5, 6, 7, 8, 9)))))
