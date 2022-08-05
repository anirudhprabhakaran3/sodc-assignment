from balg.utils import create_cubes_from_string, pretty_print
from balg.rules import apply_rules

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
    for cube in create_cubes_from_string(s):
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
    for cube in create_cubes_from_string(s):
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
    pos_cofactors = pretty_print(positive_cofactor(s, x))
    neg_cofactors = pretty_print(negative_cofactor(s, x))
    pos_cofactors = apply_rules(pos_cofactors)
    neg_cofactors = apply_rules(neg_cofactors)
    return [pos_cofactors, neg_cofactors]