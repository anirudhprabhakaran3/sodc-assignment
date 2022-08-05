from balg.utils import create_cubes_from_string, pretty_print, parse

def idempotent(s):
    cubes = create_cubes_from_string(s)
    return [*set(cubes)]

def absorption(s):
    count_dict = parse(s)
    count_list = list(count_dict.values())
    count_indexes = []
    for i in range(len(count_list)):
        if count_list[i] > 1:
            count_indexes.append(i);

    print(count_dict)
    return count_indexes

def apply_rules(s):
    s = pretty_print(idempotent(s))
    # s = pretty_print(absorption(s))
    return s