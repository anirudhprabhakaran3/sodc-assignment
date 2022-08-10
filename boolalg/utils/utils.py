def convert_string_to_cubes(s):
    """
        Input: Equation in string format
        Output: List of cubes
    """
    return s.split("+")

def order(s):
    """
        Input: List of cubes
        Output: Sorted list of cubes, based on length of SOP form.
    """
    return sorted(s, key=len)

def convert_dash_to_caps(str):
    """
        Input: String representing the equation
        Output: String without dashes, but with capitals
    """
    new_str = ""
    for i in range(len(str)):
        if str[i] == "'":
            new_str = new_str[0:-1] + new_str[-1].upper()
        else:
            new_str += str[i]
    return new_str

def remove_duplicates(s):
    """
        Input: List of cubes
        Output: List of cubes with duplicates removed.
    """
    s =  ["".join(sorted(set(x))) for x in s]
    return list(set(s))

def boolean_and(s):
    """
        Input: List of cubes
        Output: List of cubes after using boolean AND
    """
    final_cube_list = s.copy()
    for cube in s:
        if "0" in cube:
            final_cube_list.remove(cube)
        if "1" in cube:
            final_cube_list.remove(cube)
            cube = cube.replace("1", "")
            final_cube_list.append(cube)

    if len(final_cube_list) > 0:
        return final_cube_list
    else:
        return ["0"]


def boolean_or(s):
    """
        Input: List of cubes
        Output: List of cubes after using boolean OR
    """
    final_cube_list = s.copy()
    for cube in s:
        if cube == "1":
            return ["1"]
        elif cube == "0":
            final_cube_list.remove(cube)

    if len(final_cube_list) > 0:
        return final_cube_list
    else:
        return ["0"]

def process(s):
    """
        Input: Equation in form of string
        Output: Ordered list of cubes
    """
    return order(convert_string_to_cubes(convert_dash_to_caps(s)))

def boolean_fns(s):
    s = boolean_and(s)
    s = boolean_or(s)
    return s

def convert_caps_to_dash(str):
    new_str = ""
    for c in str:
        if c.isupper():
            new_str += c.lower() + "'"
        else:
            new_str += c
    return new_str

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
            print(convert_caps_to_dash(s[i]))
        else:
            print(convert_caps_to_dash(s[i]), end="+")