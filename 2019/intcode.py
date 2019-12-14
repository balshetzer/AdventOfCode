#!/usr/bin/env python3

import operator
import itertools
from collections import deque, defaultdict
from more_itertools import first

# TODO: unit tests, inpout/output adapters/conveniences, debug logging of opcodes being executed (say when different from orig prog)

class Error(Exception):
  pass

class InvalidOpcode(Error):
  def __init__(self, pc, op):
    self.pc = pc
    self.op = op

  def __str__(self):
    return ' '.join("invalid opcode", self.op, "at", self.pc)

  def __repr__(self):
    return '{0}({1],{2}})'.format(self.__name__, self.pc, self.op)

class Interpreter:
  def __init__(self, program, *, input=(), debug=False):
    if isinstance(program, str):
      program = map(int, program.split(','))
    self.mem = defaultdict(int, enumerate(program))
    self.pc = 0
    self.input = deque(input)
    self.output = deque()
    self.relative_base = 0
    self.debug = debug

  def _read_param(self, index):
    op = self.mem[self.pc]
    mode = op//(10*10**index)%10
    param = self.mem[self.pc+index]
    if mode == 0:
      return self.mem[param]
    elif mode == 1:
      return param
    elif mode == 2:
      return self.mem[param+self.relative_base]
    else:
      raise InvalidOpcode(self.pc, op)

  def _write_param(self, index, value):
    op = self.mem[self.pc]
    mode = op//(10*10**index)%10
    dest = self.mem[self.pc+index]
    if mode == 0:
      pass
    elif mode == 1:
      raise InvalidOpCode(self.pc, op)
    elif mode == 2:
      dest += self.relative_base
    else:
      raise InvalidOpcode(self.pc, op)
    self.mem[dest] = value

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

  def _relative_base_offset(self):
    self.relative_base += self._read_param(1)
    self.pc += 2

  def _halt(self):
    pass

  opcodes = {1: _add, 2: _mul, 3: _input, 4: _output, 
             5: _jump_if_true, 6: _jump_if_false, 7: _less_than, 
             8: _equals, 9: _relative_base_offset, 99: _halt}

  def step(self):
    self.opcodes[self.mem[self.pc]%100](self)

  def run(self, *, input=(), output=False):
    if (isinstance(input, int)):
      self.input.append(input)
    else:
      self.input.extend(input)
    while True:
      if output and len(self.output) > 0:
        return self.output.popleft()
      oldpc = self.pc
      self.step()
      if self.pc == oldpc:
        break

  def __iter__(self):
      return self

  def __next__(self):
    while True:
      if len(self.output) > 0:
        return self.output.popleft()
      oldpc = self.pc
      self.step()
      if self.pc == oldpc:
        raise StopIteration

  def halted(self):
    return self.mem[self.pc] == 99

  def waiting_on_input(self):
    return self.mem[self.pc] == 3

  def memory(self):
    return ','.join(str(self.mem[i]) for i in range(max(self.mem.keys())+1))
