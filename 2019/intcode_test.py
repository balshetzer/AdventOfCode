import intcode
from testutil import table

def test_state():
  def run(input, output):
    m = intcode.Interpreter(input)
    m.run()
    return m.memory()
  table(run, 
        ('1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'), 
        ('1,0,0,0,99', '2,0,0,0,99'), ('2,3,0,3,99', '2,3,0,6,99'), 
        ('2,4,4,5,99,0', '2,4,4,5,99,9801'), ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
        ('1002,4,3,4,33', '1002,4,3,4,99'), ('1101,100,-1,4,0', '1101,100,-1,4,99'))

def test_io():
  # Output its input.
  assert intcode.Interpreter('3,0,4,0,99').run(input=6, output=True) == 6
  # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
  p = '3,9,8,9,10,9,4,9,99,-1,8'
  assert intcode.Interpreter(p).run(input=8, output=True) == 1
  assert intcode.Interpreter(p).run(input=5, output=True) == 0
  # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
  p = '3,9,7,9,10,9,4,9,99,-1,8'
  assert intcode.Interpreter(p).run(input=8, output=True) == 0
  assert intcode.Interpreter(p).run(input=6, output=True) == 1
  # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
  p = '3,3,1108,-1,8,3,4,3,99'
  assert intcode.Interpreter(p).run(input=8, output=True) == 1
  assert intcode.Interpreter(p).run(input=9, output=True) == 0
  # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
  p = '3,3,1107,-1,8,3,4,3,99'
  assert intcode.Interpreter(p).run(input=8, output=True) == 0
  assert intcode.Interpreter(p).run(input=4, output=True) == 1
  # Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
  # (using position mode)
  p = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
  assert intcode.Interpreter(p).run(input=0, output=True) == 0
  assert intcode.Interpreter(p).run(input=3, output=True) == 1
  # (using immediate mode)
  p = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
  assert intcode.Interpreter(p).run(input=0, output=True) == 0
  assert intcode.Interpreter(p).run(input=3, output=True) == 1
  # This program uses an input instruction to ask for a single number. The
  # program will then output 999 if the input value is below 8, output 1000
  # if the input value is equal to 8, or output 1001 if the input value is
  # greater than 8.
  p = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
  assert intcode.Interpreter(p).run(input=2, output=True) == 999
  assert intcode.Interpreter(p).run(input=8, output=True) == 1000
  assert intcode.Interpreter(p).run(input=23, output=True) == 1001

def test_output():
  def run(p):
    m = intcode.Interpreter(p)
    m.run()
    return ','.join(str(i) for i in m.output)
  # takes no input and produces a copy of itself as output.
  p = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
  assert run(p) == p
  # output a 16-digit number
  assert run('1102,34915192,34915192,7,4,7,99,0') == '1219070632396864'
  # output the large number in the middle
  assert run('104,1125899906842624,99') == '1125899906842624'
  