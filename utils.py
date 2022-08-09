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

def remove_duplicates(s):
    """
        Input: A string
        Output: String with duplicates removed.
    """
    seen = set()
    seen_add = seen.add
    new_str = []
    for x in s:
        if x == "'":
            continue
    return "".join([x for x in s if not (x in seen or seen_add(x))])
    # str = "".join(set(s))
    # return "".join(sorted(str))

def process(s):
    """
        Input: Equation in form of string
        Output: Ordered list of cubes
    """
    return order(convert_string_to_cubes(s))