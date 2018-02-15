from z3 import *

x = FP('x', FPSort(8, 24))
y = FP('y', FPSort(8, 24))
z = FP('z', FPSort(8, 24))
assertion = Not((x + y) + z == x + (y + z))

s = Solver()
s.add(assertion)
print(s.check())
print(s.model())
