
def dict_to_list(D):
    list = []
    for key in D:
        list.append((key, D[key]))
    return list    

def list_to_dict(L):
    D = {}
    for key, value in L:
        D[key] = value
    return D
       