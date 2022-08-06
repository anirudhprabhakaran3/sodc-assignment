from utils import remove_duplicates

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
            final_list.append(remove_duplicates(cube_a+cube_b))
    return final_list

def OR(a, b):
    """
        Inputs: a and b are list of cubes
        Output: list of cubes that corresponds to a|b
    """
    return a+b

def NOT(a):
    return not a

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
                list_of_cubes.append(1)
                break
        list_of_cubes.append(cube)
    return list_of_cubes


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
                list_of_cubes.append(1)
                break
        elif x in cube:
            continue
        list_of_cubes.append(cube)
    return list_of_cubes

def cofactor(s, x):
    """
    Wrapper function to find both cofactors
    Inputs:
        s: List of cubes
        x: Literal with respect to which cofactors will be calculated
    Output: Tuple consisting of (positive cofactor, negative cofactor)
    """
    pos_cofactors = positive_cofactor(s, x)
    neg_cofactors = negative_cofactor(s, x)
    return (pos_cofactors, neg_cofactors)