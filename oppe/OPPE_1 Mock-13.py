def most_freq(M):
    parent = list()
    for x in M:
            parent.extend(x)
    unique = list(reversed(sorted(list(set(parent)))))
    y  = max(parent.count(x) for x in unique)
    for x in unique:
        if parent.count(x) == y:
            return x
    