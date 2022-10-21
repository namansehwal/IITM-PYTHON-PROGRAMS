def dim_equal(A, B):
    """
    check for dimensional equality of two matrices
    
    Arguments:
        A, B: list of lists
    Return:
        result: bool
    """
    if len(A)==len(B):
        for i in range(len(A)):
            if len(A[i])==len(B[i]):
                return True
            else:
                return False
    else:
        return False