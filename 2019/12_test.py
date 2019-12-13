from testutil import table

def test_a():
  table('12a', ('10\n' + test1, '179\n'), ('100\n' + test2, '1940\n'), ('1000\n' + input, '8538\n'))

def test_b():
  table('12b', (test1, '2772\n'), (test2, '4686774924\n'), (input, '506359021038056\n'))

input='''<x=-9, y=10, z=-1>
<x=-14, y=-8, z=14>
<x=1, y=5, z=6>
<x=-19, y=7, z=8>'''

test1='''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

test2='''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''