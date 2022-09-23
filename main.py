from boolalg.utils import process, pretty_print
from boolalg.operations import cofactor, boolean_difference, smoothing, consensus

print("RULES FOR ENTERING EQUATION")
print("1. Enter everything in lowercase, without spaces.")
print("2. Use SOP form only.")
print("3. To denote NOT a, use `a'`")
print("-"*10)

print("Enter equation:")
a = input()

print("Enter variable with respect to which cofactor has to be found: ")
x = input()

a = process(a)

pc, nc = cofactor(a, x)
bd = boolean_difference(a, x)
sm = smoothing(a, x)
cs = consensus(a, x)

pretty_print(pc, opt="Positive Cofactor:")
pretty_print(nc, opt="Negative Cofactor: ")
pretty_print(bd, opt="Boolean Difference: ")
pretty_print(sm, opt="Smoothing: ")
pretty_print(cs, opt="Consensus: ")