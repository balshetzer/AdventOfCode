import subprocess
from itertools import starmap
from more_itertools import consume

# Helpers for pytest testing

def runner(asserter, script):
  '''Return a test runner for the given script.'''
  def run(input, output):
    completed = subprocess.run("./" + script + ".py", input=input, text=True,
      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    asserter(completed.stdout.strip(), str(output))
  return run

def table(asserter, num, a, b=[]):
  script = runner(asserter, f"{num:02d}a")
  consume(starmap(script, a))
  if b:
    script = runner(asserter, f"{num:02d}b")
    consume(starmap(script, b))
