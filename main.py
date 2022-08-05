from funcs import cofactor, pretty_print

print("Enter the boolean equation")
eq = input()
print("Enter variable to find cofactor wrt")
x = input()
cofactors = cofactor(eq, x)
pretty_print(cofactors[0], opt="Positive cofactors:")
pretty_print(cofactors[1], opt="Negative cofactors:")