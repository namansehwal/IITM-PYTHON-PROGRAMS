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


def get_row(mat, row):
    """
    extract a specific row from the matrix
    
    Arguments:
        mat: list of lists
        row: integer
    Return:
        row_list: list
    """
    l=[]
    for i in range(len(mat[0])):
        l.append(mat[row][i])
    return l