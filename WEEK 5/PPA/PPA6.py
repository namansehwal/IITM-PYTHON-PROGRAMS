def type_of_sequence(L):
    """
    determine the type of a sequence
    
    Argument:
        L: list of strings
    Return:
        seq_type: string
    """
    k=0
    for i in range(len(L)):
        if mysterious(L[i]):
            k+=1
    if k<2:
        return 'mildly mysterious'
    elif k<5:
        return 'moderately mysterious'
    else:
        return 'most mysterious'