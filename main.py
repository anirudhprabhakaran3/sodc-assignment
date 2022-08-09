from utils import process, pretty_print, convert_dash_to_caps
from operations import cofactor, boolean_difference, smoothing, consensus

a = "a+b'cd'+a'd"
print(convert_dash_to_caps(a))
x='c'
a = process(a)

pc, nc = cofactor(a, x)
bd = boolean_difference(a, x)
sm = smoothing(a, x)
cs = consensus(a, x)

pretty_print(pc)
pretty_print(nc)
pretty_print(bd)
pretty_print(sm)
pretty_print(cs)