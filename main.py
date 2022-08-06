from funcs import cofactor, pretty_print, AND, OR
from rules import absoption
from utils import process

print("Enter the boolean equation")
eq = input()
print("Enter variable to find cofactor wrt")
x = input()
eq = process(eq)
cofactors = cofactor(eq, x)
pretty_print(cofactors[0], opt="Positive cofactors:")
pretty_print(cofactors[1], opt="Negative cofactors:")

print()

print("After applying rules")
pretty_print(absoption(eq))
pretty_print(absoption(cofactors[0]))
pretty_print(absoption(cofactors[1]))

print()

s1 = "ab+bc"
s2 = "cd"
s1 = process(s1)
s2 = process(s2)

pretty_print(AND(s1, s2))
pretty_print(OR(s1, s2))