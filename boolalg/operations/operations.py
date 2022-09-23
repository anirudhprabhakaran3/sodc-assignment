from boolalg.funcs import positive_cofactor, negative_cofactor
from boolalg.funcs import AND, OR, XOR
from boolalg.rules import apply_rules
from boolalg.utils import boolean_fns, order

def cofactor(s, x):
    """
    Wrapper function to find both cofactors
    Inputs:
        s: List of cubes
        x: Literal with respect to which cofactors will be calculated
    Output: Tuple consisting of (positive cofactor, negative cofactor)
    """
    pos_cofactors = order(apply_rules(positive_cofactor(s, x)))
    neg_cofactors = order(apply_rules(negative_cofactor(s, x)))
    return (pos_cofactors, neg_cofactors)

def boolean_difference(s, x):
    """
        Input: 
            s: List of cubes
            x: Variable with respect to which difference has to be found

        Output:
            List of cubes corresponding to Boolean Difference function
    """
    pos_cofactor, neg_cofactor = cofactor(s, x)
    return order(apply_rules(boolean_fns(XOR(pos_cofactor, neg_cofactor))))

def smoothing(s, x):
    """
        Input: 
            s: List of cubes
            x: Variable with respect to which difference has to be found

        Output:
            List of cubes corresponding to Smoothing function
    """
    pos_cofactor, neg_cofactor = cofactor(s, x)
    return order(apply_rules(boolean_fns(OR(pos_cofactor, neg_cofactor))))

def consensus(s, x):
    """
        Input: 
            s: List of cubes
            x: Variable with respect to which difference has to be found

        Output:
            List of cubes corresponding to Consensus function
    """
    pos_cofactor, neg_cofactor = cofactor(s, x)
    return order(apply_rules(boolean_fns(AND(pos_cofactor, neg_cofactor))))

def stringify(s):
    """
        Input:
            s: List of cubes

        Output:
            Combined string of all substrings in the list
    
    """
    return "".join(s)