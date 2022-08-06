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