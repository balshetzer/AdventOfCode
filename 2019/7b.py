#!/usr/bin/env python3

import fileinput
import operator
import itertools
from collections import deque

class Machine:
    def __init__(self, program, input, output):
        self.mem = program.copy()
        self.pc = 0
        self.input = input
        self.output = output
        
    def _read_param(self, index):
      mode = self.mem[self.pc]//(10*10**index)%10
      direct = self.mem[self.pc+index]
      if mode == 1:
          return direct
      return self.mem[direct]

    def _write_param(self, index, value):
        self.mem[self.mem[self.pc+index]] = value
    
    def _ternary(self, op):
        p1 = self._read_param(1)
        p2 = self._read_param(2)
        self._write_param(3, int(op(p1, p2)))
        self.pc += 4
        
    def _input(self):
        if (len(self.input)) == 0:
            return
        self._write_param(1, self.input.popleft())
        self.pc += 2
        
    def _output(self):
        p1 = self._read_param(1)
        self.output.append(p1)
        self.pc += 2
        
    def _add(self):
        self._ternary(operator.add)
        
    def _mul(self):
        self._ternary(operator.mul)
        
    def _jump_if(self, op):
        p1 = self._read_param(1)
        p2 = self._read_param(2)
        self.pc = p2 if op(p1) else self.pc+3
        
    def _jump_if_true(self):
        self._jump_if(operator.truth)
        
    def _jump_if_false(self):
        self._jump_if(operator.not_)

    def _less_than(self):
        self._ternary(operator.lt)
        
    def _equals(self):
        self._ternary(operator.eq)

    def _halt(self):
        pass

    opcodes = {1: _add, 2: _mul, 3: _input, 4: _output, 
               5: _jump_if_true, 6: _jump_if_false, 7: _less_than, 
               8: _equals, 99: _halt}

    def step(self):
        self.opcodes[self.mem[self.pc]%100](self)

    def run(self):
        while True:
            oldpc = self.pc
            self.step()
            if self.pc == oldpc:
                break

    def halted(self):
        return self.mem[self.pc] == 99
        
    def waiting_on_input(self):
        return self.mem[self.pc] == 3

def run_sequence(params):
    pipes = [deque([p]) for p in params]
    machines = [Machine(program, pipes[i-1], pipes[i]) for i in range(len(params))]
    pipes[-1].append(0)
    while True:
        for m in machines:
            m.run()
        if m.halted():
            return pipes[-1][0]

lines = fileinput.input()
program = list(map(int, next(lines).strip().split(',')))

print(max(map(run_sequence, itertools.permutations((5, 6, 7, 8, 9)))))
