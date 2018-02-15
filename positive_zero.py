from z3 import *

x = FP('x', FPSort(8, 24))
z = FPVal("+0.0", Float32())
assertion = (x + z == x)

s = Solver()
s.add(assertion)
print(s.check())
print(s.model())
