
import sys

def parse(s):
    """
        Takes in a string as input, and outputs all boolean literals in dictionary
    """
    literals = {}
    for i in range(len(s)):
        lit = s[i]
        if lit in ["+", "!", "(", ")", "'"]:
            continue
        if (i+1 < len(s)):
            if (s[i+1] == "'"):
                lit += "'"
                print(lit)
        if lit in literals.keys():
            literals[lit] += 1
        else:
            literals[lit] = 1
    return literals

def pretty_print(s, opt=None):
    if opt:
        print(opt, end=" ")
    for i in range(len(s)):
        if i == len(s)-1:
            print(s[i])
        else:
            print(s[i], end="+")

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return not a

def XOR(a, b):
    return (OR(AND(a, NOT(b)), AND(NOT(a), b)))

def minimisations(cube):
    if cube == "":
        return 1

def positive_cofactor(s, x):
    list_of_cubes = []
    for cube in s.split("+"):
        if (x+"'") in cube:
            continue
        elif x in cube:
            cube = cube.replace(x, "")
            if minimisations(cube) == 1:
                list_of_cubes.append(1)
                break
        list_of_cubes.append(cube)
    return list_of_cubes


def negative_cofactor(s, x):
    list_of_cubes = []
    for cube in s.split("+"):
        if (x+"'") in cube:
            cube = cube.replace((x+"'"), "")
            if minimisations(cube) == 1:
                list_of_cubes.append(1)
                break
        elif x in cube:
            continue
        list_of_cubes.append(cube)
    return list_of_cubes

def cofactor(s, x):
    pos_cofactors = positive_cofactor(s, x)
    neg_cofactors = negative_cofactor(s, x)
    return [pos_cofactors, neg_cofactors]