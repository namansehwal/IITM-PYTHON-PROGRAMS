def get_column(mat, col):
    """
    extract a specific column from the matrix

    Arguments:
        mat: list of lists
        col: integer
    Return:
        col_list: list
    """
    l=[]
    for i in range(len(mat)):
        l.append(mat[i][col])
    return l
