def most_freq(M):
    F = dict()
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] not in F:
               F[M[i][j]] = 1
            else:
                F[M[i][j]] += 1
    # print(F)
    key, value = 0, 0
    for k,v in F.items():
        if v > value:
            value = v
            key = k
        elif v == value:
            if k > key:
                value = v
                key = k
    return key