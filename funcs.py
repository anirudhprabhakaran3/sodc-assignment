from itertools import chain
from rules import apply_rules, sanitise

def parse(s):
    """
        Input: Equation in the form of string
        Output: Dict of literals and their count
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
    """
        Inputs:
            s: List of cubes to be printed in Sum of Products (SOP) form
            opt: Optional. If provided, will be printed at the beginning, and terminated with a space.
        Output:
            None
    """
    s = apply_rules(s)
    if opt:
        print(opt, end=" ")
    if len(s) == 0:
        print(0)
        return
    for i in range(len(s)):
        if i == len(s)-1:
            print(s[i])
        else:
            print(s[i], end="+")

def AND(a, b):
    """
        Inputs: a and b are list of cubes
        Output: list of cubes that corresponds to a&b
    """
    final_list = []
    for cube_a in a:
        for cube_b in b:
            final_list.append(cube_a+cube_b)
    return final_list

def OR(a, b):
    """
        Inputs: a and b are list of cubes
        Output: list of cubes that corresponds to a|b
    """
    return a+b

def NOT(a):
    """
        Input: List of cubes
        Output: List of cubes, corresponding to NOT of input
    """
    new_list = []
    for cube in a:
        notted_cube = []
        for i in cube:
            if i == "'":
                notted_cube[-1] = notted_cube[-1][0]
            else:
                notted_cube.append(i+"'")
        new_list.append(notted_cube)

    while(len(new_list) > 1):
        first = new_list[0]
        second = new_list[1]
        anded = AND(first, second)
        new_list.remove(first)
        new_list.remove(second)
        new_list.append(anded)

    return list(chain(*new_list))


def XOR(a, b):
    return (OR(AND(a, NOT(b)), AND(NOT(a), b)))

def minimisations(cube):
    """
        Input: One cube
        Output: 1 if the cube is empty.
    """
    if cube == "":
        return 1

def positive_cofactor(s, x):
    """
        Input:
            s: List of cubes
            x: Literal with respect to which positive cofactor will be calculated
        Output: List of cubes corresponding to positive cofactor
    """
    list_of_cubes = []
    for cube in s:
        if (x+"'") in cube:
            continue
        elif x in cube:
            cube = cube.replace(x, "")
            if minimisations(cube) == 1:
                list_of_cubes.append("1")
                break
        list_of_cubes.append(cube)
    if len(list_of_cubes) > 0:
        return list_of_cubes
    else:
        return ["0"]


def negative_cofactor(s, x):
    """
        Input:
            s: List of cubes
            x: Literal with respect to which negative cofactor will be calculated
        Output: List of cubes corresponding to negative cofactor
    """
    list_of_cubes = []
    for cube in s:
        if (x+"'") in cube:
            cube = cube.replace((x+"'"), "")
            if minimisations(cube) == 1:
                list_of_cubes.append("1")
                break
        elif x in cube:
            continue
        list_of_cubes.append(cube)
    if len(list_of_cubes) > 0:
        return list_of_cubes
    else:
        return ["0"]