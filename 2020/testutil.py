import subprocess
from itertools import starmap
from more_itertools import consume

def runner(script):
  '''Return a test runner for the given script.'''
  def run(input, output):
    completed = subprocess.run("./" + script + ".py", input=input, text=True, capture_output=True)
    assert completed.returncode == 0, f"Program returned {completed.returncode}: {completed.stderr}"
    assert completed.stdout == output, f"Got: '{completed.stdout}', Want: '{output}'"
  return run
  
def table(script, *cases):
  '''Run the given script against all the test cases.'''
  if isinstance(script, str):
    script = runner(script)
  consume(starmap(script, cases))
