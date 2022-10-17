def is_perfect(n):
    """
    determine if a number is perfect or not

    Argument:
        n: int
    Return:
        result: bool
    """
    fsum = 0
    for f in range(1,n):
        if n%f==0:
            fsum+=f
    return fsum==n
print(is_perfect(int(input())))