def merge(D1, D2, priority):
    if priority=='first':
        for i in D2:
            if i not in D1:
                D1[i]=D2[i]
        return D1

    if priority=='second':
        for i in D1:
            if i not in D2:
                D2[i]=D1[i]

        return D2