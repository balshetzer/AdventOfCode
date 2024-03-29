from testutil import table

def asserter(a, b):
  assert a == b

def test():
  table(asserter, 14, [(sample, 1588), (input, 2068)], [(sample, 2188189693529), (input, 2158894777814)])

sample = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

input = '''KFFNFNNBCNOBCNPFVKCP

PB -> F
KC -> F
OB -> H
HV -> N
FS -> S
CK -> K
CC -> V
HF -> K
VP -> C
CP -> S
HO -> N
OS -> N
HS -> O
HB -> F
OH -> V
PP -> B
BS -> N
VS -> F
CN -> B
KB -> O
KH -> B
SS -> K
NS -> B
BP -> V
FB -> S
PV -> O
NB -> S
FC -> F
VB -> P
PC -> O
VF -> K
BV -> K
OO -> B
PN -> N
NH -> H
SP -> B
KF -> O
BN -> F
OF -> C
VV -> H
BB -> P
KN -> H
PO -> C
BH -> O
HC -> B
VO -> O
FV -> B
PK -> V
KO -> H
BK -> V
SC -> S
KV -> B
OV -> S
HK -> F
NP -> V
VH -> P
OK -> S
SO -> C
PF -> C
SH -> N
FP -> V
CS -> C
HH -> O
KK -> P
BF -> S
NN -> O
OC -> C
CB -> O
BO -> V
ON -> F
BC -> P
NO -> N
KS -> H
FF -> V
FN -> V
HP -> N
VC -> F
OP -> K
VN -> S
NV -> F
SV -> F
FO -> V
PS -> H
VK -> O
PH -> P
NF -> N
KP -> S
CF -> S
FK -> P
FH -> F
CO -> H
SN -> B
NC -> H
SK -> P
CV -> P
CH -> H
HN -> N
SB -> H
NK -> B
SF -> H'''
