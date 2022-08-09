from funcs import positive_cofactor, negative_cofactor
from funcs import AND, OR, XOR

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

def boolean_difference(s, x):
    """
        Input: 
            s: List of cubes
            x: Variable with respect to which difference has to be found

        Output:
            List of cubes corresponding to Boolean Difference function
    """
    pos_cofactor, neg_cofactor = cofactor(s, x)
    return XOR(pos_cofactor, neg_cofactor)

def smoothing(s, x):
    """
        Input: 
            s: List of cubes
            x: Variable with respect to which difference has to be found

        Output:
            List of cubes corresponding to Smoothing function
    """
    pos_cofactor, neg_cofactor = cofactor(s, x)
    return OR(pos_cofactor, neg_cofactor)

def consensus(s, x):
    """
        Input: 
            s: List of cubes
            x: Variable with respect to which difference has to be found

        Output:
            List of cubes corresponding to Consensus function
    """
    pos_cofactor, neg_cofactor = cofactor(s, x)
    return AND(pos_cofactor, neg_cofactor)