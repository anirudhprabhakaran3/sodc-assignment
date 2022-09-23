def identity_and(s):
    """
        Input: List of cubes
        Output: List of cubes after applying aA = 0
    """
    new_cube_list = []
    for cube in s:
        flag = True
        if cube == "0" or cube == "1":
            new_cube_list.append(cube)
            continue
        for i in cube:
            if i.lower() in cube and i.upper() in cube:
                flag = False
                continue
        if flag:
            new_cube_list.append(cube)

    if len(new_cube_list) > 0:
        return new_cube_list
    else:
        return ["0"]

def identity_or(s):
    """
        Input: List of cubes
        Output: List of cubes after applying a+A = 1
    """
    single_cube_list = []
    for cube in s:
        if len(cube) == 1:
            if cube == "0" or cube == "1":
                continue
            single_cube_list.append(cube)
            x = cube.lower()
            X = cube.upper()
            if x in single_cube_list and X in single_cube_list:
                return ["1"]
    
    return s

def idempotent(s):
    """
        A+A = A
    """
    return [*set(s)]

def absorption(s):
    """
        Input: List of cubes
        Output: List of cubes after applying a+ac=a
    """
    final_cube_list = s.copy()
    for cube in s:
        temp_list = s.copy()
        temp_list.remove(cube)
        for c in temp_list:
            if cube in c:
                final_cube_list.remove(c)
    return final_cube_list

def apply_rules(s):
    """
        Wrapper function to apply all rules
        Input: List of cubes
        Output: List of cubes after applying the rules
    """
    s = identity_and(s)
    s = identity_or(s)
    s = [i for i in s if i]
    # s = absorption(s)
    s = idempotent(s)
    return s