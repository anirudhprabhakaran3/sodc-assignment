from balg.funcs import cofactor
from balg.rules import absorption, idempotent
from balg.utils import pretty_print

print("Enter the boolean equation")
eq = input()
print("Enter variable to find cofactor wrt")
x = input()
cofactors = cofactor(eq, x)
pretty_print(cofactors[0], opt="Positive cofactors:", p=True)
pretty_print(cofactors[1], opt="Negative cofactors:", p=True)

print(absorption(eq))

pretty_print(idempotent(eq), p=True)