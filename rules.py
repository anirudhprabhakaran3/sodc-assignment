def idempotent(s):
    """
        A+A = A
    """
    return [*set(s)]

def absoption(s):
    """
        A+AB = A
    """
    final_cubes = []
    ignored_indices = []
    for i in range(len(s)):
        if i in ignored_indices:
            continue
        for j in range(i+1, len(s)):
            if s[i] in s[j]:
                ignored_indices.append(j)
                continue
            else:
                final_cubes.append(s[j])
        final_cubes.append(s[i])
    return idempotent(final_cubes)

def distributive(s):
    final_cubes = []

def apply_rules(s):
    s = absoption(s)
    s = idempotent(s)
    return s

def boolean_not(cube):
    if "0'" in cube:
        cube.replace("0'", "1")
    if "1'" in cube:
        cube.replace("1'", "0")
    return cube

def boolean_and(cube):
    if "0" in cube:
        cube = "0"
    if "1" in cube:
        cube.replace("1", "")
    return cube

def boolean_or(s):
    for i in s:
        if i == 1:
            return ["1"]
        
        if i == 0:
            s.remove(i)
    return s

def sanitise(s):
    s = [boolean_and(boolean_not(x)) for x in s]
    return boolean_or(s)