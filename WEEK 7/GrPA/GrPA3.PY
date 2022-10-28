def minor_matrix(M, i, j):
    l=[]
    for a in range(len(M)):
        t=[]
        if a==i:
            continue
        else:
            for b in range(len(M[0])):
                if b==j:
                    continue
                else:
                    t.append(M[a][b])
        l.append(t)
    return l