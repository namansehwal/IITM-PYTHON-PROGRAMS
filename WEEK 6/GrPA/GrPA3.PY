def rotate(mat):
    """
    Rotate a matrix 90 degrees clockwise
    
    Argument:
        mat: list of lists
    Return:
        rotated_mat: list of lists
    """
    rotated_mat = []
    for i in range(len(mat[0])):
        turned = []
        for j in mat[::-1]:
            turned.append(j[i])
        rotated_mat.append(turned)
    
    return rotated_mat
