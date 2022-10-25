def value_to_keys(D, value):
    
    keys = []
    for key in D:
        if D[key] == value:
            keys.append(key)
    return keys