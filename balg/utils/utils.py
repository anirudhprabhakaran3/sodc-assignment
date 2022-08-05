def create_cubes_from_string(s):
    return s.split("+")

def pretty_print(s, opt=None, p=False):
    output = ""
    if opt:
        output = output + opt + " "
    for i in range(len(s)):
        if i == len(s)-1:
            output += s[i] + "\n"
        else:
            output += s[i] + "+"
    if p:
        print(output)
    return output

def parse(s):
    """
        Takes in a string as input, and outputs all boolean literals in dictionary
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