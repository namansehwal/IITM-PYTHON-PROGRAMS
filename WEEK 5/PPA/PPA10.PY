def insert(L, x):
    """
    insert an element x into a sorted list L

    Arguments:
        L: list
        x: integers
    Return:
        sorted_L: list
    """
    L.append(x)
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
    return L