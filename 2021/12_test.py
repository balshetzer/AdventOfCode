from testutil import table

def asserter(a, b):
  assert a == b

def test():
  table(asserter, 12, [(small, 10), (medium, 19), (large, 226), (input, 4691)], [(small, 36), (medium, 103), (large, 3509), (input, 140718)])

small = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

medium = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

large = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

input = '''dr-of
start-KT
yj-sk
start-gb
of-start
IJ-end
VT-sk
end-sk
VT-km
KT-end
IJ-of
dr-IJ
yj-IJ
KT-yj
gb-VT
dr-yj
VT-of
PZ-dr
KT-of
KT-gb
of-gb
dr-sk
dr-VT'''
