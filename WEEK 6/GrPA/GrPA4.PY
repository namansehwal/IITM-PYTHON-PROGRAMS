def two_level_sort(scores):
    """
    Perform a two-level sort

    Argument: 
        scores: list of tuples, (string, integer)
    Return:
        result: list of tuples (string, integer)
    """
    result = []
    for i, e in enumerate(scores):
        if i == 0:
            result.append(e)
        else:
            for j, f in enumerate(result):
                if e[1] > f[1]:
                    result.insert(j, e)
                    break
                elif j == len(result) - 1:
                    result.append(e)
    
print(two_level_sort([('a', 1), ('b', 1), ('c', 2), ('d', 2), ('e', 3), ('f', 3)]))