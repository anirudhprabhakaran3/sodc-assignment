from rules import apply_rules
from utils import remove_duplicates

def AND(a, b):
    """
        Inputs: a and b are list of cubes
        Output: list of cubes that corresponds to a&b
    """
    final_list = []
    for cube_a in a:
        for cube_b in b:
            final_list.append(cube_a+cube_b)
    return remove_duplicates(final_list)

def OR(a, b):
    """
        Inputs: a and b are list of cubes
        Output: list of cubes that corresponds to a|b
    """
    return remove_duplicates(a+b)

def NOT(a):
    """
        Input: List of cubes
        Output: List of cubes, corresponding to NOT of input
    """
    new_list = []
    for cube in a:
        notted_cube = []
        for i in cube:
            if i == "0":
                notted_cube.append("1")
            elif i == "1":
                notted_cube.append("0")
            elif i.isupper():
                notted_cube.append(i.lower())
            else:
                notted_cube.append(i.upper())
        new_list.append(notted_cube)

    while(len(new_list) > 1):
        first = new_list[0]
        second = new_list[1]
        new_list.append(AND(first, second))
        new_list.remove(first)
        new_list.remove(second)
    
    return remove_duplicates(new_list[0])


def XOR(a, b):
    return OR(AND(a, NOT(b)), AND(NOT(a), b))

def positive_cofactor(s, x):
    """
        Input:
            s: List of cubes
            x: Literal with respect to which positive cofactor will be calculated
        Output: List of cubes corresponding to positive cofactor
    """

    list_of_cubes = []
    X = x.upper()
    x = X.lower()

    for cube in s:
        if X in cube:
            continue
        if x in cube:
            cube = cube.replace(x, "")
            if cube == "":
                cube = "1"
        list_of_cubes.append(cube)

    if "1" in list_of_cubes:
        list_of_cubes = ["1"]

    list_of_cubes = remove_duplicates(list_of_cubes)

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
    X = x.upper()
    x = X.lower()

    for cube in s:
        if x in cube:
            continue
        if X in cube:
            cube = cube.replace(X, "")
            if cube == "":
                cube = "1"
        list_of_cubes.append(cube)

    if "1" in list_of_cubes:
        list_of_cubes = ["1"]

    list_of_cubes = remove_duplicates(list_of_cubes)
        
    if len(list_of_cubes) > 0:
        return list_of_cubes
    else:
        return ["0"]