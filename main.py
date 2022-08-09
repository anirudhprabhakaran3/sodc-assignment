from utils import process
from operations import cofactor, boolean_difference, consensus, smoothing

eq1 = "ab"
eq2 = "ab"
x = "b"
eq1 = process(eq1)
eq2 = process(eq2)

print(eq1)
print(x)

print()

pc, nc = cofactor(eq1, x)
bd = boolean_difference(eq1, x)
sm = smoothing(eq1, x)
cs = consensus(eq1, x)

print(nc)
print(pc)
print(bd)
print(sm)
print(cs)