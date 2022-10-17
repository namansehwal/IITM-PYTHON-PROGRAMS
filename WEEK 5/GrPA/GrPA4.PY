def is_magic(mat):
    """
    determine if a matrix is magic square

    Argument:
        mat: list of lists
    Return:
        string: 'YES' or 'NO'
    """
    m = len(mat)
    d1sum, d2sum = 0, 0
    for i in range(m):
        d1sum += mat[i][i]
        d2sum += mat[i][m - i - 1]
    if not(d1sum == d2sum):
        return 'NO'
    for i in range(m):
        rsum, csum = 0, 0
        for j in range(m):
            rsum += mat[i][j]
            csum += mat[j][i]
        if not(rsum == csum == d1sum):
            return 'NO'
    return 'YES'